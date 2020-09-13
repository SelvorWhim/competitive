# assuming non-overlapping and initially sorted

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        found = False
        
        # todo: optimize with binary search, since they're sorted
        for i in range(len(intervals)):
            # insert case:
            if newInterval[1] < intervals[i][0]:
                found = True
                intervals.insert(i,newInterval)
                break
            
            # merge case:
            if newInterval[0] <= intervals[i][1]:
                found = True
                intervals[i][0] = min(newInterval[0], intervals[i][0])
                intervals[i][1] = max(newInterval[1], intervals[i][1])
                # merge with interval(s) ahead too:
                while (len(intervals) > i + 1) and (newInterval[1] >= intervals[i+1][0]):
                    intervals[i][1] = max(newInterval[1], intervals[i+1][1])
                    del intervals[i+1]
                break
        
        # insert last case:
        if not found:
            intervals.append(newInterval)
        
        return intervals
