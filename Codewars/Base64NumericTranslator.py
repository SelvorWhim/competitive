BASE_MAP = {c:i for i,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")}
BASE = len(BASE_MAP) # 64

def base64_to_base10(str):
    res = 0
    for c in str:
        res *= BASE
        res += BASE_MAP[c]
    return res
