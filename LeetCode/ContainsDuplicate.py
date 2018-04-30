# NOTE: the first solution is slower on given test cases, despite stopping immediately on finding a duplicate while the second solution goes over entire list
'''
class OldSolution:
    # O(n) solution using Python set
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in nums:
            if i in seen: # amortized O(1) containment check
                return True
            seen.add(i)  # amortized O(1)
        return False
'''

class Solution:
    # O(n) solution using Python set
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))
