import pytest


@pytest.fixture(autouse=True)
def _test_env(monkeypatch):
    monkeypatch.setenv("PROD_ALMA_API_KEY", "fake-key")
    monkeypatch.setenv("SANDBOX_ALMA_API_KEY", "fake-key")
