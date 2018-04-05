class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return [0,0]
        
        a = ord('a')
        max_line = 100
        
        line_count = 1
        curr_line = 0
        for c in S:
            w = widths[ord(c)-a] # assuming all characters are lowercase latin letters
            if curr_line + w > max_line:
                line_count += 1
                curr_line = w
            else:
                curr_line += w
        return [line_count, curr_line]
