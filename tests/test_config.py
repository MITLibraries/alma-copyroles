import pytest

from copyroles.config import Config


@pytest.fixture
def config_instance():
    return Config()


def test_prod_alma_api_key_raises_error(monkeypatch, config_instance):
    monkeypatch.delenv("PROD_ALMA_API_KEY")
    with pytest.raises(OSError, match="Env var 'PROD_ALMA_API_KEY' must be defined"):
        _ = config_instance.prod_alma_api_key


def test_sandbox_alma_api_key_raises_error(monkeypatch, config_instance):
    monkeypatch.delenv("SANDBOX_ALMA_API_KEY")
    with pytest.raises(OSError, match="Env var 'SANDBOX_ALMA_API_KEY' must be defined"):
        _ = config_instance.sandbox_alma_api_key


def test_check_required_env_vars(monkeypatch, config_instance):
    monkeypatch.delenv("SANDBOX_ALMA_API_KEY")
    with pytest.raises(OSError, match="Missing required environment variables:"):
        config_instance.check_required_env_vars()
