# from every index you can jump up to its value to the right
# iterate indexes and break if you reach an index that's further than you can jump
# just keep track of what's the furthest to the right you can jump up to now

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for curr_i, delta in enumerate(nums):
            if max_reachable < curr_i:
                return False
            max_reachable = max(max_reachable, curr_i + delta)
        return True # reached end index without breaking
