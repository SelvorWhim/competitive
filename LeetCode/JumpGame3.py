# next moves depend only on what index you're at, so let's check which indexes are reachable and stop whenever we find one with value 0

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.reachable = [False] * len(arr)
        return self.can_reach_recursive(arr, start)
    
    def can_reach_recursive(self, arr: List[int], start: int):
        if start < 0 or start >= len(arr): # bad index
            return False
        if arr[start] == 0: # found it!
            return True
        if self.reachable[start]: # use memoization to stop exponential growth
            return False
        self.reachable[start] = True
        return self.can_reach_recursive(arr, start + arr[start]) or self.can_reach_recursive(arr, start - arr[start])
