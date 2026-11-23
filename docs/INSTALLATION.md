# Installation

Requirements: Python 3.12+ and Nmap installed separately. Create a virtual environment, install `python -m pip install -r requirements.txt`, then run `python -m app.main`. The UI listens at `http://127.0.0.1:8080`; the database is created on first launch.

## Windows 10/11

Install Nmap from [nmap.org/download.html](https://nmap.org/download.html), including Npcap if prompted. In PowerShell run `py -3.12 -m venv .venv`, `.venv\Scripts\Activate.ps1`, install requirements, then start the app. If Nmap is not on PATH, set `nmap_path` in `app/config.py`. Administrator rights may be needed for SYN scans, OS detection, and some discovery modes.

## Ubuntu

Run `sudo apt update` and `sudo apt install python3 python3-venv nmap`. Then `python3 -m venv .venv`, `source .venv/bin/activate`, install requirements, and launch. Raw packet features may need root or suitable capabilities.

## Debian

Run `sudo apt update` and `sudo apt install python3 python3-venv nmap`, then follow the Ubuntu virtual-environment steps. Prefer narrowly scoped Nmap capabilities over running the web application as root.

PyInstaller may package Python code per operating system, but Nmap/Npcap remains an external dependency.
