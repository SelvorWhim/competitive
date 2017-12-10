# idea: the sum of minimums will be bigger if we pair the smallest n amongst themselves and the biggest n amongst themselves than with each other. Extrapolating (without formal proof), I think the sum will be biggest if the list is sorted and then paired up in order.

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # assuming list doesn't need to be preserved, otherwise extra space is needed
        return sum([nums[i] for i in range(0,len(nums),2)])
