
# SHICTHRSENCR\SHICTHRSENCR\utils\identity\SHRENCR_check_nickname.py

import re

def check_nickname(nickname : str) -> bool:
    if not isinstance(nickname, str):
        return False
    
    nickname = nickname.strip()
    
    if not nickname:
        return False
    
    if len(nickname) > 20:
        return False
    
    if len(nickname) < 1:
        return False
    
    pattern = r'^[a-zA-Z0-9\u4e00-\u9fff]+$'
    
    return bool(re.fullmatch(pattern, nickname))