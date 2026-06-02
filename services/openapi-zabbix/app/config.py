from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações do serviço Zabbix."""

    zabbix_url: str = "http://zabbix.local/api_jsonrpc.php"
    zabbix_api_token: str = ""
    verify_ssl: bool = True
    timeout_seconds: float = 20.0

    model_config = SettingsConfigDict(
        env_prefix="",
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
