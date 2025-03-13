import os
from collections.abc import Iterable


class Config:
    REQUIRED_ENV_VARS: Iterable[str] = [
        "PROD_ALMA_API_KEY",
        "SANDBOX_ALMA_API_KEY",
    ]

    def check_required_env_vars(self) -> None:
        """Method to raise exception if required env vars not set."""
        missing_vars = [var for var in self.REQUIRED_ENV_VARS if not os.getenv(var)]
        if missing_vars:
            message = f"Missing required environment variables: {', '.join(missing_vars)}"
            raise OSError(message)

    def get_alma_api_key(self, environment: str) -> str:
        if environment == "sandbox":
            return self.sandbox_alma_api_key
        if environment == "prod":
            return self.prod_alma_api_key
        error_message = f"Alma environment '{environment}' not recognized."
        raise ValueError(error_message)

    @property
    def alma_api_endpoint(self) -> str:
        return os.getenv(
            "ALMA_API_ENDPOINT", "https://api-na.hosted.exlibrisgroup.com/almaws/v1/"
        )

    @property
    def prod_alma_api_key(self) -> str:
        value = os.getenv("PROD_ALMA_API_KEY")
        if not value:
            error_message = "Env var 'PROD_ALMA_API_KEY' must be defined"
            raise OSError(error_message)
        return value

    @property
    def sandbox_alma_api_key(self) -> str:
        value = os.getenv("SANDBOX_ALMA_API_KEY")
        if not value:
            error_message = "Env var 'SANDBOX_ALMA_API_KEY' must be defined"
            raise OSError(error_message)
        return value
