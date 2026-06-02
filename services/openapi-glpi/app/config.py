from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações do serviço GLPI.

    Os valores devem vir de variáveis de ambiente ou do arquivo deploy/.env
    quando usado via Docker Compose.
    """

    glpi_url: str = "http://glpi.local/apirest.php"
    glpi_app_token: str = ""
    glpi_user_token: str = ""
    verify_ssl: bool = True
    timeout_seconds: float = 20.0

    model_config = SettingsConfigDict(
        env_prefix="",
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
