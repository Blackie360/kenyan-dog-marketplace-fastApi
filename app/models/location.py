from pydantic import BaseModel, Field
from typing import Optional
from ..utils.constants import VALID_KENYA_COUNTIES

class Location(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    city: str
    county: str = Field(..., description="Must be a valid Kenyan county")
    
    def validate_county(self):
        if self.county not in VALID_KENYA_COUNTIES:
            raise ValueError(f"Invalid county. Must be one of: {', '.join(VALID_KENYA_COUNTIES)}")