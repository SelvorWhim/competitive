class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colornum = 3 # easily adjustable for a similar task with more colors
        counts = colornum*[0]
        for i in nums:
            counts[i] += 1
        sofar = 0
        for i in range(colornum):
            ci = counts[i]
            nums[sofar:sofar+ci] = ci*[i]
            sofar += ci
