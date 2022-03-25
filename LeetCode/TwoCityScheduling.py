class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort by amount of extra cost by interviewing in a instead of b.
        costs.sort(key=lambda cost: cost[0] - cost[1])
        # the n with the smallest diff should be interviewed in a, the rest in b.
        n = len(costs) // 2
        return sum(cost[0] for cost in costs[:n]) + sum(cost[1] for cost in costs[n:])
