# idea: find an interval in which each letter appears, then merge intersecting intervals
# since we are going over the string in order to create the intervals, we can keep them ordered, making merging easier

from collections import OrderedDict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # construct intervals:
        letter_intervals = OrderedDict()
        for i, c in enumerate(S):
            if c not in letter_intervals:
                # 1st appearance
                letter_intervals[c] = [i,i] # set start and end of interval
            else:
                letter_intervals[c][1] = i # update only end of interval
        
        # merge intervals:
        intervals = list(letter_intervals.values())
        n = len(intervals)
        for i in range(n - 1, 0, -1): # iterate indexes backward se we can merge as we go
            if intervals[i-1][1] >= intervals[i][0]: # if overlap, merge to first in pair and delete 2nd
                intervals[i-1] = [intervals[i-1][0], max(intervals[i-1][1], intervals[i][1])]
                del intervals[i]
        intervals_lens = [(interval[1] - interval[0] + 1) for interval in intervals]
        return intervals_lens
