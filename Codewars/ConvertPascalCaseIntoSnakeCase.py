def map_letter(c):
    return "_" + c.lower() if c.isupper() else c

def to_underscore(s):
    return str.lstrip("".join(map_letter(c) for c in str(s)), "_")
