vowels = 'aeiou'

def count_vowels(s: str) -> int:
    count = 0
    for c in s.lower():
        if c in vowels:
            count += 1
    return count

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return count_vowels(s[:len(s)//2]) == count_vowels(s[len(s)//2:])
