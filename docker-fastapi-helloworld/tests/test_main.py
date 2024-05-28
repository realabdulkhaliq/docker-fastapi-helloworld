from fastapi.testclient import TestClient
from docker_fastapi_helloworld.main import app

def test_root_path():
    client = TestClient(app=app)
    responce = client.get("/")
    assert responce.status_code == 200
    assert responce.json() == {"Hello":"World"}