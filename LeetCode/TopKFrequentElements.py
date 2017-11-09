from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        topK_pairs = Counter(nums).most_common(k) # for k<<n complexity is apparently O(n*log(k)) which is better than O(n*log(n)) but not quite linear
        return [pair[0] for pair in topK_pairs]
