fix = {'5':'S', '0':'O', '1':'I'}

def correct(s):
    return "".join(fix.get(c, c) for c in s)
