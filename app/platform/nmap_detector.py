import shutil
import nmap

def detect_nmap(configured_path: str | None = None) -> dict[str, str | bool | None]:
    path = configured_path or shutil.which("nmap")
    if not path:
        return {"available": False, "path": None, "version": None, "error": "Nmap executable was not found."}
    try:
        scanner = nmap.PortScanner(nmap_search_path=(path,))
        version = scanner.nmap_version()
        return {"available": True, "path": path, "version": ".".join(map(str, version)), "error": None}
    except (nmap.PortScannerError, OSError) as exc:
        return {"available": False, "path": path, "version": None, "error": str(exc)}
