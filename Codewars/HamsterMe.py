# idea: build an encoder for the full alphabet and use it
# (could also find nearest key character for every character in the message, but the alphabet is small so that would probably be more complex)

def hamster_me(code, message):
    keys = set(code)
    enc = {c:c+"1" for c in keys}
    last_key_c = min(keys) # could be any, really, we're looping
    first = ord(last_key_c)
    i = first + 1 # iterates character code (ord) in a loop around the alphabet
    while i != first:
        c = chr(i)
        if c in keys:
            last_key_c = c
        else:
            enc[c] = last_key_c + str((i - ord(last_key_c))%26 + 1)
        if c < "z":
            i += 1
        else:
            i = ord("a")
    return "".join(enc[c] for c in message)
