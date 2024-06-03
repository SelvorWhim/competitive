# since it's only appending to the end, scan s to find as many characters of t in order as possible, and append the rest

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i_t = 0
        i_s = 0
        for i_s in range(len(s)):
            if s[i_s] == t[i_t]:
                i_t += 1
                if i_t >= len(t):
                    # found all of t in s, so already a subsequence
                    return 0
        # found i_t of the characters, append the rest
        return len(t) - i_t
