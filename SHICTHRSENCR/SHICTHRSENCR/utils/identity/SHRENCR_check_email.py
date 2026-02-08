
# SHICTHRSENCR\SHICTHRSENCR\utils\identity\SHRENCR_check_email.py

import re

def check_email(email : str) -> bool:
    if not isinstance(email , str):
        return False
    
    email = email.strip()
    
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return bool(re.fullmatch(pattern , email))