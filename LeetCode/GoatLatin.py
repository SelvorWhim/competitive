vowels = ["a","e","i","o","u"]

# assumes non-empty word made of letters (follows from assumptions on input and whitespace split)
# does the conversion not including adding "ma" and more "a"s
def wordToGoatLatin(word):
    return word if word[0].lower() in vowels else word[1:] + word[0]

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        return " ".join([wordToGoatLatin(words[i]) + "ma" + (i+1)*"a" for i in range(len(words))])
