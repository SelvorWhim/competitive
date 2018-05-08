from collections import Counter

def duplicate_count(text):
    return len([1 for count in Counter(text.lower()).values() if count > 1])
