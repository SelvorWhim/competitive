from collections import Counter

def duplicate_count(text):
    return len([1 for letter,count in Counter(text.lower()).items() if count > 1])
