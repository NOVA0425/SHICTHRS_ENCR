
# SHICTHRSENCR\SHICTHRSENCR\utils\identity\SHRENCR_check_wx_identity_number.py

import re

def check_wx_identity_number(identity_number : str) -> bool:
    if not isinstance(identity_number, str):
        return False
    
    identity_number = identity_number.strip()
    
    if not identity_number:
        return False
    
    if len(identity_number) > 20:
        return False
    
    if len(identity_number) < 6:
        return False
    
    pattern = r'^[a-zA-Z][a-zA-Z0-9_-]{5,19}$'
    
    return bool(re.fullmatch(pattern, identity_number))