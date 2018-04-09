def hex_digit(d):
    return chr(ord('A')+(d-10)) if d > 9 else str(d)

def hex_val(n):
    if n >= 255:
        return "FF"
    if n <= 0:
        return "00"
    return hex_digit(n // 16) + hex_digit(n % 16)

def rgb(r, g, b):
    #return hex_val(r) + hex_val(g) + hex_val(b)
    return "".join([hex_val(v) for v in [r,g,b]]) # oh look at me, so DRY that it's longer than the repetitive original :P
