import json
from app.reporting.json_exporter import export_json

def test_json_export(tmp_path):
    path=tmp_path/"out.json"; export_json({"hosts":[]},path)
    assert json.loads(path.read_text())=={"hosts":[]}
