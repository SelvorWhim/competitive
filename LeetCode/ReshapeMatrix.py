class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        x = len(nums)
        y = len(nums[0]) if x > 0 else 0
        if x*y != r*c:
            return nums
        listnums = [item for row in nums for item in row]
        return [listnums[i*c:i*c+c] for i in range(r)]
