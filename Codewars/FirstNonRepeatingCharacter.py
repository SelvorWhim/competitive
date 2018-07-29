from collections import Counter

def first_non_repeating_letter(string):
    cs = Counter(string.lower())
    for c in string:
        if cs[c.lower()] == 1: # ignore letter case when counting
            return c # but output original case
    return ""
