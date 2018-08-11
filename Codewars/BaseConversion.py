# string in base (defined by alphabet) to integer
def map_from_base(s, base = bin):
    b = len(base)
    n = 0
    base_to_digit = {c:i for i,c in enumerate(base)}
    for c in s:
        n *= b
        n += base_to_digit[c]
    return n

# integer to string in base (defined by alphabet)
def map_to_base(n, base = bin):
    b = len(base)
    sd = []
    while n > 0:
        sd.append(base[n % b])
        n //= b
    return "".join(sd[::-1]) if sd else base[0]

def convert(input, source, target):
    return map_to_base(map_from_base(input, source), target)
