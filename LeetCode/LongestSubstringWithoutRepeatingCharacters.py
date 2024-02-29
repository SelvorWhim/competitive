class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars_in_curr_substr = set()
        left_i = 0
        for i in range(len(s)):
            if s[i] not in chars_in_curr_substr:
                chars_in_curr_substr.add(s[i])
                res = max(res, len(chars_in_curr_substr))
            else:
                while s[i] != s[left_i]:
                    chars_in_curr_substr.remove(s[left_i])
                    left_i += 1
                left_i += 1
        return res

