# for each substring of equal consecutive letters, omit all but the first 2

class Solution:
    def makeFancyString(self, s: str) -> str:
        included_chars = [s[0]]
        last_char_count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                last_char_count += 1
            else:
                last_char_count = 1
            if last_char_count <= 2:
                included_chars.append(s[i])
        return "".join(included_chars)
