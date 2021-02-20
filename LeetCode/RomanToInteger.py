roman_value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # idea: roman numerals add the values of symbols independently, unless a smaller symbol appears before a larger.
        # not every combination of symbols is valid, but if we assume valid input, this rule should suffice.
        prev_value = 0
        total = 0
        for c in s:
            curr_value = roman_value[c]
            if curr_value > prev_value:
                total -= 2*prev_value
            total += curr_value
            prev_value = curr_value
        return total
