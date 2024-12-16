import re
from typing import Optional
from ..utils.constants import PHONE_PREFIXES

def validate_phone(phone: str) -> bool:
    """Validate Kenyan phone numbers."""
    # Remove any spaces or dashes
    phone = phone.replace(" ", "").replace("-", "")
    
    # Check if the number starts with valid prefixes
    has_valid_prefix = any(phone.startswith(prefix) for prefix in PHONE_PREFIXES)
    
    # Convert to standard format (254XXXXXXXXX)
    if phone.startswith("0"):
        phone = "254" + phone[1:]
    elif phone.startswith("+"):
        phone = phone[1:]
    
    # Check length and format
    phone_pattern = r'^254[17]\d{8}$'
    return has_valid_prefix and bool(re.match(phone_pattern, phone))