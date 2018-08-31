oa = ord('a')

def word_score(word):
    return sum((ord(letter) - oa + 1) for letter in word)

def high(s):
    print(s)
    return max(s.split(), key=word_score)
