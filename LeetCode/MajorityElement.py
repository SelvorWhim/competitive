from collections import Counter
class Solution:
    # lazy solution that works if majority element exists (not hard to check for one if necessary). Should be O(n) time, and anywhere from O(1) to O(k) space depending on most_common implementation, for k number of unique elements
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]
