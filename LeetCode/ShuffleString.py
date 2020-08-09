class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s) # assumed to be the same as len(indices)
        shuffled_s = ["0"]*n
        for i in range(n):
            shuffled_s[indices[i]] = s[i]
        return "".join(shuffled_s)
