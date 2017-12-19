# assuming words contain alphabetical only
from collections import Counter

ORD_A = ord('a')
ORD_Z = ord('z')
ALPHABET_LEN = ORD_Z - ORD_A + 1

# alphabetic, lowercase
def letter_counter(word):
    c = [0]*ALPHABET_LEN
    for l in word.lower():
        i = ord(l)
        if i >= ORD_A and i <= ORD_Z:
            c[i - ORD_A] += 1
    return c

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        c0 = letter_counter(licensePlate)
        first = True
        shortest = ""
        for word in words:
            if (not first) and len(word) >= len(shortest):
                continue
            c1 = letter_counter(word)
            valid_so_far = True
            for i in range(ALPHABET_LEN):
                if c1[i] < c0[i]: # not enough of a required letter
                    valid_so_far = False
                    break
            if valid_so_far:
                first = False
                shortest = word
        return shortest
