from app.database.models import Scan, Host, Port

def test_core_models_have_expected_tables(): assert (Scan.__tablename__,Host.__tablename__,Port.__tablename__)==("scans","hosts","ports")
