class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        # one iteration for each spiral
        while left <= right and top <= bottom:
            # right:
            ret += matrix[top][left:right+1]
            top += 1
            if top > bottom:
                break
            # down:
            ret += [row[right] for row in matrix[top:bottom+1]]
            right -= 1
            if left > right:
                break
            # left:
            ret += matrix[bottom][left:right+1][::-1]
            bottom -= 1
            if top > bottom:
                break
            # up:
            ret += [row[left] for row in matrix[top:bottom+1][::-1]]
            left += 1
        return ret
