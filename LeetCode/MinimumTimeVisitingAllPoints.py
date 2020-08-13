# oh whew we're going in order, I nearly read this as travelling salesman

# minimum steps between two points. You can do diagonals so whichever dimension has the biggest distance determines the steps
def minSteps(p1, p2):
    return max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(1, len(points)):
            total_time += minSteps(points[i-1], points[i])
        return total_time
