from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # read env variables
    # we could add another .env variable (.env.prod). In this case the latter takes
    # precedent over the former (env_file=(".env", ".env.prod"))
    model_config = SettingsConfigDict(env_file="...env", extra="ignore")
    app_name: str = "Tech-Hub"
    

settings = Settings()