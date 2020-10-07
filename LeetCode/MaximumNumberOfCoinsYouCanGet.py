# sort, then for each trio pick the top 2 remaining and the bottom 1
# thus, minimize differences between top and 2nd pile to minimize coins lost to Alice
# and maximize differences between 2nd and 3rd to maximize coins won from Bob

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort(reverse=True)
        return sum(piles[1:2*(n//3):2])
