# CDN Real Scanner

A fast, multi-threaded Python CLI tool for scanning CDN IP ranges on ports 80 and 443. Optimized for Termux on Android.

---

## Features

- Multi-threaded scanning (up to 100 threads)
- Scans ports 80 and 443
- Live progress bar with real-time results
- Auto-saves working hosts to a file
- Safe thread limit for Termux compatibility
- Simple CLI interface — no external dependencies

---

## Termux Install Guide

### 1. Install Termux

Download Termux from [F-Droid](https://f-droid.org/packages/com.termux/) (recommended) or the Play Store.

### 2. Update packages and install Python

```bash
pkg update && pkg upgrade -y
pkg install python -y
```

### 3. Clone or copy the tool

```bash
# If you have git installed:
pkg install git -y
git clone https://github.com/YOUR_USERNAME/cdn-real-scanner.git
cd cdn-real-scanner

# Or manually create the file:
nano scanner.py
# Paste the contents of scanner.py, then save with Ctrl+X → Y → Enter
```

### 4. Make the script executable (optional)

```bash
chmod +x scanner.py
```

### 5. Run the scanner

```bash
python scanner.py
```

> No packages need to be installed — the tool uses Python's built-in standard library only.

---

## Example Usage

```
$ python scanner.py

  ____  ____  _   _     ____                  _
 / ___||  _ \| \ | |   / ___|  ___ __ _ _ __ | |
| |    | | | |  \| |   \___ \ / __/ _` | '_ \| |
| |___ | |_| | |\  |    ___) | (_| (_| | | | |_|
 \____||____/|_| \_|   |____/ \___\__,_|_| |_(_)

        CDN Real Scanner - Fast Port Scanner
        Optimized for Termux | Ports: 80, 443

Enter IP range (CIDR format, e.g. 104.21.96.0/24): 104.21.96.0/24
Enter output file path (e.g. results.txt): open_hosts.txt

[*] Target range : 104.21.96.0/24
[*] Hosts to scan: 254
[*] Ports        : 80, 443
[*] Threads      : 100
[*] Output file  : open_hosts.txt
[*] Started at   : 2026-04-15 10:00:00
------------------------------------------------------------
[########################################] 100.0% | OPEN  104.21.96.1:80
[########################################] 100.0% | OPEN  104.21.96.1:443

============================================================
[+] Scan complete!
[+] Total scanned : 508 checks
[+] Open ports    : 2
[+] Results saved : open_hosts.txt
[+] Finished at   : 2026-04-15 10:00:12
============================================================

[+] Working hosts:
    104.21.96.1:80
    104.21.96.1:443
```

---

## Supported CDN IP Ranges

Use any of these CIDR ranges as input:

### Cloudflare

| Range              |
|--------------------|
| 103.21.244.0/22    |
| 103.22.200.0/22    |
| 103.31.4.0/22      |
| 104.16.0.0/13      |
| 104.24.0.0/14      |
| 108.162.192.0/18   |
| 131.0.72.0/22      |
| 141.101.64.0/18    |
| 162.158.0.0/15     |
| 172.64.0.0/13      |
| 173.245.48.0/20    |
| 188.114.96.0/20    |
| 190.93.240.0/20    |
| 197.234.240.0/22   |
| 198.41.128.0/17    |

### Google / Google Cloud CDN

| Range              |
|--------------------|
| 8.8.4.0/24         |
| 8.8.8.0/24         |
| 34.64.0.0/10       |
| 35.184.0.0/13      |
| 130.211.0.0/22     |
| 142.250.0.0/15     |
| 172.217.0.0/16     |
| 209.85.128.0/17    |
| 216.58.192.0/19    |

### Amazon CloudFront

| Range              |
|--------------------|
| 13.32.0.0/15       |
| 13.35.0.0/16       |
| 52.84.0.0/15       |
| 54.182.0.0/16      |
| 54.192.0.0/16      |
| 64.252.64.0/18     |
| 70.132.0.0/18      |
| 99.84.0.0/16       |
| 143.204.0.0/16     |
| 205.251.192.0/19   |

---

## Notes

- No external Python packages required — uses only the standard library.
- The tool respects Termux's thread limits. The default cap is 100 threads.
- Results are saved in real time as open ports are found — safe even if the scan is interrupted.
- Only use this tool on IP ranges you own or have explicit permission to scan.

---

## Project Structure

```
cdn-real-scanner/
├── scanner.py       # Main scanner script
├── requirements.txt # No dependencies (standard library only)
└── README.md        # This file
```

---

## License

MIT
