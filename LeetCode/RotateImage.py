# idea: rotate clockwise = transpose + horizontal flip, which can both be easily implemented in place by switching pairs of elements.
# to do this one operation in place, we would need to shift elements around 4 at a time (and select the right 4 elements), which seems more complicated, and I doubt it would save much time, if any

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # assuming square
        
        # transpose:
        for i in range(n):
            for j in range(i): # lower triangle
                # switch:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # horizontal flip:
        for i in range(n):
            for j in range(n//2): # if n is odd, the middle column is untouched - that's fine
                # switch:
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = temp
        
        # matrix is modified in-place, no return
