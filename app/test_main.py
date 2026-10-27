from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_whoami_uses_account_name(monkeypatch):
    monkeypatch.setenv("ACCOUNT_NAME", "prod")
    assert client.get("/whoami").json()["account"] == "prod"
