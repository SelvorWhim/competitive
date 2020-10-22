from re import search

def increment_string(s):
    num_match = search(r"(0|[1-9]\d*)$", s)
    str_end = num_match.start() if num_match else len(s)
    num = int(num_match.group()) if num_match else 0
    if (str_end > 0 and s[str_end-1] == '0' and len(str(num+1)) > len(str(num))):
        str_end -= 1
    return s[:str_end] + str(num+1)
