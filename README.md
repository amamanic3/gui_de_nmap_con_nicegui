# Nmap Network Discovery GUI

A local Python application scaffold for authorized network discovery and inventory. NiceGUI provides the interface; python-nmap is isolated behind the scanner layer; SQLAlchemy stores scan observations in SQLite.

Included: dark dashboard and inventory pages, validated scan requests, fixed safe profiles, background worker execution, historical host/port observations, whitelist matching, compatibility reporting, PyVis host graph, and CSV/JSON export. This is an initial implementation; NSE controls, durable job recovery, UI cancellation, full traceroute workflows, a scan comparison screen, and PDF/XML UI export remain future work. Topology emits no invented edges.

See [docs/INSTALLATION.md](docs/INSTALLATION.md). Install Nmap separately, create a Python 3.12+ environment, install `requirements.txt`, then run `python -m app.main` from this directory. The server binds to localhost by default. No scan runs at startup. Only scan systems and ranges you are authorized to assess.
1. Install **Python 3.12+** and **Nmap** (include Npcap on Windows).
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:
   - Windows: `py -3.12 -m venv .venv` then `.venv\Scripts\Activate.ps1`
   - Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `python -m pip install -r requirements.txt`
5. Start the app: `python -m app.main`
6. Open **http://127.0.0.1:8080** in your browser.