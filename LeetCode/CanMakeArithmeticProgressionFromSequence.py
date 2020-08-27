# naive approach: sort array and check if the sorted version is an arithmetic progression

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return True
        sorted_arr = sorted(arr)
        d = sorted_arr[1] - sorted_arr[0]
        for i in range(2, len(sorted_arr)):
            if sorted_arr[i] - sorted_arr[i-1] != d:
                return False
        return True
