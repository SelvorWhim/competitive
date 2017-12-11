# assumes words have at least 1 letter and are alphabetic and that the keyboard layout is QWERTY

rows = [{"q","w","e","r","t","y","u","i","o","p"},
        {"a","s","d","f","g","h","j","k","l"},
        {"z","x","c","v","b","n","m"}]

def find_row(letter):
    for i in range(len(rows)):
        if letter in rows[i]:
            return i
    raise ValueError('Not a lowercase latin letter')

def is_single_row(word):
    first_letter_row = find_row(word[0].lower())
    for letter in word[1:]:
        if find_row(letter.lower()) != first_letter_row:
            return False
    return True

class Solution:
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word for word in words if is_single_row(word)]
