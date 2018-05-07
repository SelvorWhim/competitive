from collections import Counter

def isValidWalk(walk):
    if len(walk) != 10:
        return False
    c = Counter(walk)
    return c['n'] == c['s'] and c['e'] == c['w']
