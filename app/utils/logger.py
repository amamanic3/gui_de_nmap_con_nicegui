from loguru import logger
from app.config import ROOT

def configure_logging() -> None:
    log_dir = ROOT / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    logger.add(log_dir / "nmap-gui.log", rotation="5 MB", retention="10 days", level="INFO")
