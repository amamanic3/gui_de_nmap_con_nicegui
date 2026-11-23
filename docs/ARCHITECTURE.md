# Architecture

NiceGUI pages call application services; pages do not invoke Nmap. `ScanService` creates the scan record and coordinates `ScanManager`; the manager dispatches blocking python-nmap calls to a thread pool. `NmapEngine` validates requests, chooses a fixed profile, calls python-nmap, and sends results to the normalizer.

SQLAlchemy models and repositories live in `database`; `HostObservation` associates hosts and port rows to a specific scan, preserving historical results. Whitelist and comparison logic are application services. Reporting serializes normalized data. Graph building emits observed host nodes without unsupported links.

Flow: UI → Pydantic validation/service → scan record → worker manager → Nmap engine → normalized results → persistence → inventory/history/export. Jobs currently live in memory. The schema includes scans, hosts, observations, ports, services, groups, whitelist devices, comparisons, traceroute hops, and NSE results.
