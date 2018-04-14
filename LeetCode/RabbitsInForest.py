# the description is a bit ambiguous, but going by the example, it can be generalized - the minimum number with the information given is, for every answer that's the same number, the number of answerers plus 1, sum over all answer numbers
# except that if you have 3 answers saying 1, they can't all refer to the same color - for every color with an answer of 1 we can have at most 2 answerers falling in that group. In that case the minimum would be 4.

from collections import Counter

class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        c = Counter(answers)
        sum = 0
        for n in c: # n is the number given, and c[n] is the number of answerers who gave it
            sum += c[n] - (c[n]%(n+1)) # split the equal-answerers into the max groups that can refer to the same color
            if c[n] % (n+1) > 0:
                sum += n+1 # then add a group (color) for any remaining and add the size of that group to account for remainder
        return sum
