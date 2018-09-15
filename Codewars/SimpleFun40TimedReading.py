import re

def timed_reading(max_length, text):
    return len([word for word in re.split(r'\W+', text) if 0 < len(word) <= max_length])
