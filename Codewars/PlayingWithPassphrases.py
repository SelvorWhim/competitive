class PassphraseMapper(object):
    def __init__(self, n):
        self.n = n
    
    def __getitem__(self, c):
        c = chr(c)
        if c.islower():
            return chr(ord('a')+(ord(c)-ord('a')+self.n)%26) # circular shift for lowercase letters
        if c.isupper():
            return chr(ord('A')+(ord(c)-ord('A')+self.n)%26) # circular shift for uppercase letters
        if c.isdigit():
            return str(9 - int(c)) # complement to 9
        return c

def play_pass(s, n):
    step3 = s.translate(PassphraseMapper(n))
    step4 = "".join([step3[i].upper() if i%2==0 else step3[i].lower() for i in range(len(step3))])
    return step4[::-1]
