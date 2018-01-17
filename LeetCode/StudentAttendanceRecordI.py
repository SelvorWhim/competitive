class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0
        l_streak = 0
        for c in s:
            if c == 'A':
                if a_count >= 1:
                    return False
                a_count += 1
            if c == 'L':
                if l_streak >= 2:
                    return False
                l_streak += 1
            else:
                l_streak = 0
        return True
