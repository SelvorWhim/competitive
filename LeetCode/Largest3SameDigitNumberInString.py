class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best_so_far = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                best_so_far = max(best_so_far, num[i : i+3])
        return best_so_far
