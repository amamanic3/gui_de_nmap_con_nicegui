# Troubleshooting

- **Nmap missing:** install Nmap, reopen the shell, or configure `nmap_path`.
- **Permission error:** TCP connect scans usually work as a standard user. SYN, UDP, OS fingerprinting, and raw discovery may need administrator/root rights or Linux capabilities.
- **No hosts found:** verify the CIDR, route, interface, and firewall. ICMP may be blocked; no reply does not prove a host is offline.
- **Interface details sparse:** install optional `psutil` for richer interface metadata.
- **Database error:** verify `data/` is writable and back up before repair.
- **Scan failed:** inspect History and `logs/nmap-gui.log`; check Nmap version, authorization, and timeout.
- **Export failed:** verify `reports/` is writable and the filename is valid.
- **Graph issue:** verify PyVis is installed and use a modern browser; current graph contains host nodes only.
