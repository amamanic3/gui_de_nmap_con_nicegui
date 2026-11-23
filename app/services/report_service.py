from pathlib import Path
from app.config import settings
from app.reporting.csv_exporter import export_csv
from app.reporting.json_exporter import export_json

class ReportService:
    def export(self, kind: str, rows: list[dict], filename: str) -> Path:
        name=Path(filename).name
        if not name or name in {".",".."}: raise ValueError("Choose a valid filename.")
        settings.report_dir.mkdir(parents=True,exist_ok=True); path=settings.report_dir/name
        if kind=="csv": export_csv(rows,path)
        elif kind=="json": export_json(rows,path)
        else: raise ValueError("Supported exports: CSV and JSON.")
        return path
