# idea: find an interval in which each letter appears, then merge intersecting intervals
# since we are going over the string in order to create the intervals, we can keep them ordered, making merging easier

from collections import OrderedDict

# adapted from: https://www.geeksforgeeks.org/merging-intervals/
# assumes intervals are sorted by interval start, and all values are non-negative
# (in this problem they represent indexes, so they are)
def merge_overlapping_intervals(intervals): 
    ret = [] 
    curr_start = -1
    curr_end = -1
    for i in range(len(intervals)): 
        curr_interval = intervals[i] 
        if curr_interval[0] > curr_end: 
            if i > 0: 
                ret.append([curr_start, curr_end]) 
            curr_end = curr_interval[1] 
            curr_start = curr_interval[0] 
        else: 
            if curr_interval[1] >= curr_end: 
                curr_end = curr_interval[1] 
    if curr_end >= 0 and [curr_start, curr_end] not in ret: 
        ret.append([curr_start, curr_end])
    return ret

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
        merged_intervals = merge_overlapping_intervals(intervals)
        intervals_lens = [(interval[1] - interval[0] + 1) for interval in merged_intervals]
        return intervals_lens
