class Solution:
    romanVals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # idea: roman numerals add the values of symbols independently, unless a smaller symbol appears before a larger.
        # not every combination of symbols is valid, but if we assume valid input, this rule should suffice.
        sum = 0
        lastVal = 10000
        for sym in s:
            currVal = Solution.romanVals[sym]
            if currVal <= lastVal:
                sum += currVal
            else:
                sum += currVal - (2*lastVal) # undo addition of symbol that turns out to be "negative" valued
            lastVal = currVal
        return sum
