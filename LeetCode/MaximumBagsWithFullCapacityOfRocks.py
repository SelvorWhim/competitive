class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining_capacities_sorted = sorted([capacity[i] - rocks[i] for i in range(len(capacity))])
        filled_bags = 0
        for remaining in remaining_capacities_sorted:
            if additionalRocks < remaining:
                return filled_bags
            additionalRocks -= remaining
            filled_bags += 1
        return filled_bags
