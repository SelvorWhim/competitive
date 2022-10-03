"""
idea: for minimum time, will have to remove all but one of each run of a color
so best to remove all but the one that requires the most time
"""

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last_run_color = ''
        last_run_total = 0
        last_run_max = 0
        total = 0
        for i in range(len(colors)):
            if colors[i] == last_run_color:
                last_run_total += neededTime[i]
                last_run_max = max(last_run_max, neededTime[i])
            else:  # just switched run (or it's the first run)
                total += last_run_total - last_run_max
                last_run_color = colors[i]
                last_run_total = neededTime[i]
                last_run_max = neededTime[i]
        total += last_run_total - last_run_max  # since there was no switch from the last run
        return total
