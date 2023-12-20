class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Need top 2, there's definitely a more efficient way but this is simplest
        prices.sort()
        cost_of_2 = prices[0] + prices[1]
        if cost_of_2 > money:
            return money
        return money - cost_of_2
