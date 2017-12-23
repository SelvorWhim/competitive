''' 717. 1-bit and 2-bit Characters '''
# the representations form a prefix code, so strings have unambiguous decodings
# assuming bits contains only 0's and 1's.
# given that the last character is a 0, and a 0 always ends a character, and a 1 only ends a character of length 2, we can start from the end and check whether it is preceded by an even or odd number of 1's - if even, then the 0 must be 1-bit, and if odd, the 0 must be the end of a 2-bit character.

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 0 or bits[-1] == 1: # we assume it's a 0 but just in case
            return False
        even = True
        for bit in bits[-2::-1]: # bits in reverse except the last
            if bit == 1:
                even = not even # flip, maintaining parity count for number of 1's
            else: # interested only in run of 1's preceding last 0
                break
        return even
