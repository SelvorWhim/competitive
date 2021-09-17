from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common_counter = Counter(nums1) & Counter(nums2)
        ret = []
        for n, count in common_counter.items():
            ret.extend(count * [n])
        return ret
