from math import ceil

def caesar_letter(c, shift):
    oa = ord("A") if c.isupper() else ord("a")
    return chr(oa + (ord(c) - oa + shift) % 26)

# adds shift (can be used for encoding and decoding); doesn't split
def moving_caesar(s, shift, reverse = False):
    sign = -1 if reverse else 1
    return "".join(caesar_letter(c,shift + sign*i) if c.isalpha() else c for i,c in enumerate(s))

def moving_shift(s, shift):
    enc = moving_caesar(s, shift)
    elen = int(ceil(len(s)/5.0)) # even/equal length
    return ["".join(sub) for sub in (enc[i*elen:(i+1)*elen] for i in range(5))]

def demoving_shift(s, shift):
    return moving_caesar("".join(s), -shift, True)
