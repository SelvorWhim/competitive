# pretty sure you can flip the sign of any even number of cells with an unlimited number of moves like this
# in which case, if there's an even number of negative cells you can turn them all positive
# and if there's an odd number, you can turn all but the number with the smallest absolute value positive, to maximize the sum.

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_sum = sum(sum(abs(cell) for cell in row) for row in matrix)
        nonpositive_cell_count = sum(sum(1 for cell in row if cell <= 0) for row in matrix)
        if nonpositive_cell_count % 2 == 1:
            smallest_abs_value = min(min(abs(cell) for cell in row) for row in matrix)
            abs_sum -= 2 * smallest_abs_value
        return abs_sum
