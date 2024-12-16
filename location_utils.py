from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="dog_marketplace")

def get_coordinates(location: str):
    try:
        loc = geolocator.geocode(location)
        if loc:
            return loc.latitude, loc.longitude
        return None, None
    except Exception as e:
        print(f"Error getting coordinates for {location}: {e}")
        return None, None
