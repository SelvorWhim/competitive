def next_looknsay(a_curr):
    a_next = ""
    d_curr = a_curr[0]
    d_count = 0
    for d in a_curr:
        if d == d_curr:
            d_count += 1
        else:
            a_next += str(d_count) + d_curr
            d_count = 1
            d_curr = d
    a_next += str(d_count) + d_curr
    return a_next

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        a_i = str(1)
        for i in range(1,n):
            a_i = next_looknsay(a_i)
        return a_i
