# we're either turning it into a "0101..." string or a "1010..." string, count the changes needed for each

class Solution:
    def minOperations(self, s: str) -> int:
        even_index_one_changes = s[0::2].count('0') + s[1::2].count('1')
        even_index_zero_changes = s[1::2].count('0') + s[0::2].count('1')
        return min(even_index_one_changes, even_index_zero_changes)
