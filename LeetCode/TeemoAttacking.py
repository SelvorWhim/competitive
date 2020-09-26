class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        total_poisoned = 0
        for i in range(len(timeSeries)-1):
            total_poisoned += min(duration, timeSeries[i+1] - timeSeries[i])
        total_poisoned += duration
        return total_poisoned
