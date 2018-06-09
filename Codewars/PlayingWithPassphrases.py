class PassphraseMapper(object):
    def __init__(self, n):
        self.n = n
    
    def __getitem__(self, c):
        c = chr(c)
        if c.isalpha(): # circular shift for letters
            a = ord('a') if c.islower() else ord('A')
            return chr(a + ((ord(c) - a + self.n) % 26))
        if c.isdigit(): # complement to 9 for digits
            return str(9 - int(c))
        return c # leave the rest as is

def play_pass(s, n):
    step3 = s.translate(PassphraseMapper(n)) # steps 1-3 (out of context character translation)
    step4 = "".join([step3[i].upper() if (i % 2 == 0) else step3[i].lower() for i in range(len(step3))]) # step 4 (character capitalization by index)
    return step4[::-1] # step 5 (reversal)
