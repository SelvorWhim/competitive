"""
Idea: on instantiation, save a matrix where each cell has the sum
of the rectangle starting at the top left corner and ending at
the equivalent cell in the original matrix.
On query, calculate the arbitrary rectangle sum based on that sum-from-top-left
minus the sum of the rectangle above it and the rectangle to the left,
plus the rectangle above and to the left to account for double subtraction.
Complexity: O(m*n) space, O(m*n) initialization and O(1) for subsequent queries
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumFromCorner = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            row = n*[0]
            runningRowSum = 0
            for j in range(n):
                runningRowSum += matrix[i][j]
                row[j] = (self.sumFromCorner[i-1][j] if i > 0 else 0) + runningRowSum
            self.sumFromCorner.append(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topRectSum = self.sumFromCorner[row1 - 1][col2] if row1 > 0 else 0
        leftRectSum = self.sumFromCorner[row2][col1 - 1] if col1 > 0 else 0
        topLeftRectSum = self.sumFromCorner[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.sumFromCorner[row2][col2] - leftRectSum - topRectSum + topLeftRectSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
