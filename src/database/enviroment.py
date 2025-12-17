from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseEnviroment(BaseSettings):
    POSTGRESQL_URL_INTERNAL: str = ''
    POSTGRESQL_URL_EXTERNAL: str = ''
    model_config = SettingsConfigDict(
        env_file='.env'
    )