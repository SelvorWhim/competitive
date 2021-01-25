class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        seen_1 = False
        dist_from_last_1 = 0
        for num in nums:
            if num == 0:
                dist_from_last_1 += 1
            else:
                if seen_1 and dist_from_last_1 < k:
                    return False
                dist_from_last_1 = 0
                seen_1 = True
        return True
