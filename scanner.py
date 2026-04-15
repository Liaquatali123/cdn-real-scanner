#!/usr/bin/env python3

import socket
import ipaddress
import threading
import sys
import os
from queue import Queue
from datetime import datetime

PORTS = [80, 443]
MAX_THREADS = 100
TIMEOUT = 2

lock = threading.Lock()
results = []
scanned = 0
total = 0


def check_host(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((str(ip), port))
        sock.close()
        return result == 0
    except Exception:
        return False


def worker(queue, output_file):
    global scanned
    while True:
        item = queue.get()
        if item is None:
            queue.task_done()
            break

        ip, port = item
        is_open = check_host(ip, port)

        with lock:
            scanned += 1
            progress = int((scanned / total) * 40)
            bar = "[" + "#" * progress + "-" * (40 - progress) + "]"
            percent = (scanned / total) * 100

            if is_open:
                entry = f"{ip}:{port}"
                results.append(entry)
                print(f"\r{bar} {percent:.1f}% | OPEN  {entry}          ")
                with open(output_file, "a") as f:
                    f.write(entry + "\n")
            else:
                sys.stdout.write(
                    f"\r{bar} {percent:.1f}% | Scanned {scanned}/{total} hosts"
                )
                sys.stdout.flush()

        queue.task_done()


def get_ip_list(cidr):
    network = ipaddress.ip_network(cidr, strict=False)
    return list(network.hosts())


def print_banner():
    banner = r"""
  ____  ____  _   _     ____                  _
 / ___||  _ \| \ | |   / ___|  ___ __ _ _ __ | |
| |    | | | |  \| |   \___ \ / __/ _` | '_ \| |
| |___ | |_| | |\  |    ___) | (_| (_| | | | |_|
 \____||____/|_| \_|   |____/ \___\__,_|_| |_(_)

        CDN Real Scanner - Fast Port Scanner
        Optimized for Termux | Ports: 80, 443
"""
    print(banner)


def main():
    print_banner()

    cidr = input("Enter IP range (CIDR format, e.g. 104.21.96.0/24): ").strip()
    if not cidr:
        print("No IP range provided. Exiting.")
        sys.exit(1)

    try:
        ip_list = get_ip_list(cidr)
    except ValueError as e:
        print(f"Invalid CIDR: {e}")
        sys.exit(1)

    output_file = input("Enter output file path (e.g. results.txt): ").strip()
    if not output_file:
        output_file = "results.txt"

    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    open(output_file, "w").close()

    global total
    total = len(ip_list) * len(PORTS)

    thread_count = min(MAX_THREADS, total)

    print(f"\n[*] Target range : {cidr}")
    print(f"[*] Hosts to scan: {len(ip_list)}")
    print(f"[*] Ports        : {', '.join(str(p) for p in PORTS)}")
    print(f"[*] Threads      : {thread_count}")
    print(f"[*] Output file  : {output_file}")
    print(f"[*] Started at   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    queue = Queue()

    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(queue, output_file), daemon=True)
        t.start()
        threads.append(t)

    for ip in ip_list:
        for port in PORTS:
            queue.put((ip, port))

    for _ in range(thread_count):
        queue.put(None)

    queue.join()

    print(f"\n\n{'=' * 60}")
    print(f"[+] Scan complete!")
    print(f"[+] Total scanned : {scanned} checks")
    print(f"[+] Open ports    : {len(results)}")
    print(f"[+] Results saved : {output_file}")
    print(f"[+] Finished at   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    if results:
        print("\n[+] Working hosts:")
        for r in results:
            print(f"    {r}")


if __name__ == "__main__":
    main()
