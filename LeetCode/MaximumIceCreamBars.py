class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_buyable = 0
        # Buy them from cheapest to most expensive until you run out of coins.
        for cost in sorted(costs):
            coins -= cost
            if coins < 0:
                break
            max_buyable += 1
        return max_buyable
