# Administrator guide

Install Python requirements in a virtual environment and install Nmap separately. Configure database URL, report folder, Nmap path, binding, timeout, and worker limit in `app/config.py`; default binding is loopback. SQLite is created at `data/nmap.db`. Stop the application before copying the file for a simple backup. Models retain per-scan observations. `create_all` initializes schemas; `database/migrations.py` is only a hook and should be upgraded to versioned migrations before schema changes are deployed.

Logs rotate under `logs/`; report files are under `reports/`. Restrict both directories according to local policy. Privileged scanning depends on Nmap, Npcap, Linux capabilities, and network policy. Prefer least privilege. Job state currently resides in memory; restart recovery is not implemented.
