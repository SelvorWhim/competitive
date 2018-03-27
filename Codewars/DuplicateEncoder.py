from collections import Counter

def duplicate_encode(word):
    ctr = Counter(word.lower())
    return "".join(["(" if ctr[l.lower()] == 1 else ")" for l in word])