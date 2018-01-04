# idea: the smallest cookie will, at best, satisfy the least greedy child, and if not, we may as well throw it away, since we can't add it to another cookie
# likewise for every cookie from the smallest. By extension, there's no reason to try satisfying a more greedy child before the least greedy
# so sort both groups ascending, and go through cookies until the least greedy child left is satisfied, then move on to the next child and continue with the remaining cookies

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s) < 1:
            return 0
        g.sort() # kids
        s.sort() # cookies
        ik = 0
        ic = 0
        sat = 0
        while ik < len(g) and ic < len(s):
            if g[ik] <= s[ic]:
                sat += 1
                ik += 1
            ic += 1
        return sat
