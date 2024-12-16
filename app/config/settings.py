from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Kenya Dog Marketplace API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "API for connecting dog buyers and sellers in Kenya with geolocation support"
    
    # Kenya's boundaries
    KENYA_MIN_LAT: float = -4.678
    KENYA_MAX_LAT: float = 5.506
    KENYA_MIN_LON: float = 33.908
    KENYA_MAX_LON: float = 41.899

settings = Settings()