from app import app
def test_health():
 c=app.test_client(); assert c.get('/health').status_code==200
def test_version(monkeypatch):
 monkeypatch.setenv('APP_VERSION','test-version')
 c=app.test_client(); assert c.get('/version').get_json()=={'version':'test-version'}
