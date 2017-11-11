class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for linear time, can't use anything based on a comparison sort.
        # Here range is limited, so something linear-time is plausible, but only with extra space.
        # Just based on the amount of info, it has to be linear space.
        # So my first idea should be optimal, up to a constant: keep an array of what we've seen, and look for the member that wasn't
        n = len(nums)
        seen = [False] * (n+1) # initialize array of the value False of length n+1
        for i in nums:
            seen[i] = True # n items will be marked True. By input assumptions, all indexes will be in range
        for i in range(n+1):
            if not seen[i]:
                return i
