# we've got every combination of horizontal and vertical cuts, so the biggest area(/volume) should simply be the widest segment between horizontal cuts times the widest segment between vertical cuts

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        full_horizontal_cuts = [0] + sorted(horizontalCuts) + [h]
        full_vertical_cuts = [0] + sorted(verticalCuts) + [w]
        max_horizontal_segment = max(full_horizontal_cuts[i] - full_horizontal_cuts[i-1] for i in range(1, len(full_horizontal_cuts)))
        max_vertical_segment = max(full_vertical_cuts[i] - full_vertical_cuts[i-1] for i in range(1, len(full_vertical_cuts)))
        return (max_horizontal_segment * max_vertical_segment) % (10**9 + 7)
