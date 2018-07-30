OA = ord("A")
A_LEN = 26 # alphabet length

# Assumes uppercase letter. Works with negative shift too.
def shift_letter(letter, shift):
    return chr(OA + (ord(letter) - OA + shift) % A_LEN)

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, s, shift = None):
        shift = shift or self.shift
        return "".join([shift_letter(c.upper(), shift) if c.isalpha() else c for c in s])
        
    def decode(self, s):
        return self.encode(s, -self.shift)
