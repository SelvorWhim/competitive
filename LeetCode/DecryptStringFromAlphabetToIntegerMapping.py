def numToLetter(n):
    """ for 1 <= n <= 26 """
    return chr(ord('a') + n - 1)

class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = []
        n = len(s)
        i = 0
        while i < n:
            if i >= n-2 or s[i+2] != '#':
                letters.append(numToLetter(int(s[i])))
                i += 1
            else:
                letters.append(numToLetter(int(s[i:i+2])))
                i += 3 # skip '#'
        return ''.join(letters)
