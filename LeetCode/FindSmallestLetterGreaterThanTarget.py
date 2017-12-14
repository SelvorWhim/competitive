# assumes all letters are lowercase alphabetical (all uppercase should work too, but not mixed or any other characters or non-characters)

ALPHABET_LEN = ord('z') - ord('a') + 1

def dist_to_letter(target, letter):
    if target == letter:
        return ALPHABET_LEN # because it must be strictly "bigger", the target itself is furthest
    return (ord(letter) - ord(target) + ALPHABET_LEN) % ALPHABET_LEN

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        best_l = letters[0]
        best_d = dist_to_letter(target, letters[0])
        for l in letters[1:]:
            d = dist_to_letter(target, l)
            if d < best_d:
                best_d = d
                best_l = l
        return best_l
