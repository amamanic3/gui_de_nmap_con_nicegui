import json
from pathlib import Path

def export_json(data, path: Path) -> None: path.write_text(json.dumps(data,indent=2,default=str),encoding="utf-8")
