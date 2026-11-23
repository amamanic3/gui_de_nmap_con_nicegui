import csv
from pathlib import Path

def export_csv(rows: list[dict], path: Path) -> None:
    fields=list(dict.fromkeys(k for row in rows for k in row))
    with path.open("w",newline="",encoding="utf-8-sig") as stream:
        writer=csv.DictWriter(stream,fieldnames=fields); writer.writeheader(); writer.writerows(rows)
