from app import app


def test_health():
    client = app.test_client()
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json() == {'status': 'UP'}


def test_quote_default():
    client = app.test_client()
    res = client.get('/quote')
    assert res.status_code == 200
    j = res.get_json()
    assert 'from' in j and 'to' in j and 'price' in j and 'timestamp' in j