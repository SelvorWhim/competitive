import re

def alphanumeric(s):
    return re.match(r"^[a-zA-Z0-9]+$", s) != None
