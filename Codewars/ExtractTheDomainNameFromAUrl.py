import re

def domain_name(url):
    pattern = r"^(?:[a-zA-Z]+://)?(?:www\.)?([-\w]+)\..+$"
    return re.match(pattern, url).group(1) # assuming URL scheme fits one of the patterns in test cases
