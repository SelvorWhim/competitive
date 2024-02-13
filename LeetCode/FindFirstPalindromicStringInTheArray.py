def is_palindrome(s: str):
    # those indexes took some fiddling, a loop would probably be clearer
    # but this works efficiently for both even and odd length strings
    return s[:len(s)//2] == s[:(len(s)-1)//2:-1]

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if is_palindrome(word):
                return word
        return ""
