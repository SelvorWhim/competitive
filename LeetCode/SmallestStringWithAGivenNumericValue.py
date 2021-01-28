# we want as many 'a's at the start as possible, and for that as many 'z's at the end as possible
# and whatever is needed in the middle to make up the difference

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n > k or 26*n < k:
            raise ValueError('impossible!')
        k -= n # work with values where a is 0 and z is 25
        num_z = k // 25
        num_a = max(0, n - num_z - 1)
        mid_val = chr(ord('a') + k % 25) if num_z < n else ''
        return num_a*'a' + mid_val + num_z*'z'
