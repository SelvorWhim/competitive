from collections import Counter

def scramble(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    for l in c2:
        if c1[l] < c2[l]:
            return False
    return True
