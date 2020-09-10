from collections import Counter

def matching_spots(s1, s2):
    return sum(s1[i]==s2[i] for i in range(len(s1)))

def matching_unordered(c1, c2):
    return sum(min(c1[d], c2[d]) for d in c1.keys())

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = matching_spots(secret, guess)
        cows_and_bulls = matching_unordered(Counter(secret), Counter(guess))
        cows = cows_and_bulls - bulls
        return '{}A{}B'.format(bulls, cows)
