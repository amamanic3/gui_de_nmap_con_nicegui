# User manual

Open the local URL printed at startup. Sidebar sections include Dashboard, Scanner, Discovery, Hosts, Whitelist, Topology, History, Reports, and Settings. Ports and services are at `/ports`. The application does not scan automatically.

## Scanner and discovery

Enter an IP, hostname, or CIDR, select a profile, optionally provide ports as `22,80,443` or `1-1024`, confirm authorization, and start. Ping does host discovery only; Common TCP and Service TCP inspect common ports; UDP Common may need elevated privileges. Discovery submits ping discovery. Blocked probes can make live devices appear unresponsive. Current progress is recorded as job status; live progress and UI cancellation are not implemented yet.

## Inventory and authorization

Hosts lists addresses, hostnames, MAC addresses, state, OS estimate, and last observation. Ports lists observed states and service metadata. Whitelist registers a device with at least one identifier and compares inventory. Unmatched hosts are unclassified, not malicious. Import/export and edit/delete controls are not implemented.

## Topology and history

Topology shows host nodes only and never infers links from address proximity. History lists scans. A comparison service exists but no comparison screen is currently connected.

## Reports

Reports exports host inventory as CSV or JSON to `reports/`. XML/PDF helpers exist but are not exposed in this interface yet. Keep the report directory access controlled.

## Settings and errors

Settings displays OS, Nmap executable/version, interfaces, and privilege summary. If Nmap is missing, install it and ensure PATH or `nmap_path` is correct. A missing ping response is not proof of an offline host; filtered port states are inconclusive. For failures, check target syntax, permissions, timeout, `logs/nmap-gui.log`, and [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
