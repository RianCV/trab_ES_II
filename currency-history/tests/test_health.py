from app import app


def test_health():
    client = app.test_client()
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json() == {'status': 'UP'}


def test_history_default():
    client = app.test_client()
    res = client.get('/history')
    assert res.status_code == 200
    j = res.get_json()
    assert 'values' in j and isinstance(j['values'], list)