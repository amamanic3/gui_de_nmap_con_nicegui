from pathlib import Path
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent.parent

class Settings(BaseModel):
    database_url: str = f"sqlite:///{(ROOT / 'data' / 'nmap.db').as_posix()}"
    report_dir: Path = ROOT / "reports"
    max_concurrent_scans: int = Field(default=2, ge=1, le=8)
    scan_timeout_seconds: int = Field(default=900, ge=10, le=7200)
    # nmap_path: str | None = None
    nmap_path: str | None = "C:\\Program Files (x86)\\Nmap\\nmap"
    bind_host: str = "192.168.0.14"
    bind_port: int = Field(default=8080, ge=1024, le=65535)

settings = Settings()
