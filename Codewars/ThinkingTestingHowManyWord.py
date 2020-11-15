def testit(s):
    key = 'word'
    letter_i = 0
    for c in s:
        if c.lower() == key[letter_i % len(key)]:
            letter_i += 1
    return letter_i // len(key)
