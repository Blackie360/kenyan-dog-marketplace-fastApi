from typing import Tuple
from math import radians, sin, cos, sqrt, atan2
from ..config.settings import settings

def is_within_kenya(lat: float, lon: float) -> bool:
    """Check if coordinates are within Kenya's boundaries."""
    return (settings.KENYA_MIN_LAT <= lat <= settings.KENYA_MAX_LAT and
            settings.KENYA_MIN_LON <= lon <= settings.KENYA_MAX_LON)

def calculate_distance(
    point1: Tuple[float, float],
    point2: Tuple[float, float]
) -> float:
    """
    Calculate distance between two points using Haversine formula.
    Returns distance in kilometers.
    """
    EARTH_RADIUS = 6371  # Earth's radius in kilometers
    
    lat1, lon1 = map(radians, point1)
    lat2, lon2 = map(radians, point2)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    
    return EARTH_RADIUS * c