class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # calculate max height for every row and column (O(m*n))
        row_maxs = [max(row) for row in grid]
        col_maxs = [max([row[i] for row in grid]) for i in range(len(grid[0]))] # grid guaranteed at least 1x1
        ret = 0
        # find how much we can to each building without increasing the max height at its row or column, thus without changing skyline (O(m*n))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret += min(row_maxs[i], col_maxs[j]) - grid[i][j] # at least 0
        return ret
