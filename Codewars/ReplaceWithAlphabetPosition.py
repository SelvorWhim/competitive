def letter_pos(l):
    return ord(l.lower())-ord('a') + 1

def alphabet_position(text):
    return " ".join([str(letter_pos(c)) for c in text if c.isalpha()])
