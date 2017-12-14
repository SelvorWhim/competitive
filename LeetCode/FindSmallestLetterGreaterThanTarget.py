# assumes all letters are lowercase alphabetical (all uppercase should work too, but not mixed or any other characters or non-characters)

from bisect import bisect # binary search

'''
ALPHABET_LEN = ord('z') - ord('a') + 1

def dist_to_letter(target, letter):
    if target == letter:
        return ALPHABET_LEN # because it must be strictly "bigger", the target itself is furthest
    return (ord(letter) - ord(target) + ALPHABET_LEN) % ALPHABET_LEN
'''

class Solution:
    # non-optimized v1 - does not take pre-sort into account. O(n) time, O(1) space. Of course, if letters are non-repeating, n<=26 so it's no big deal. In fact, overhead for a more asymptotically optimized solution might make actual complexity worse
    '''
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
    '''
    
    # optimized v2 - O(log(n)) time, O(1) space
    # idea: letters are sorted alphabetically, but due to wraparound distance is not quite. However, it would be enough to find the closest letter and take the next one if it's smaller or equal, wrapping around if necessary
    def nextGreatestLetter(self, letters, target):
        i = bisect(letters, target) # this variant returns index just after any appearance of target or anything smaller - perfect. No option for a key function but default comparator works on characters as necessary
        return letters[0] if i >= len(letters) else letters[i]