"""
there are much fewer operations than potential places modified
more efficient to look up the last operation that modified a given index
(or original value if it wasn't modified) than to keep values updated all the time.
In practice we'd probably run the heavy computation to update
once in a while / in the background to reduce the length of self.ops
"""

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.ops = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.ops.append((row1, col1, row2, col2, newValue))

    @staticmethod
    def is_in_rect(row: int, col: int, row1: int, col1: int, row2: int, col2: int):
        return row1 <= row <= row2 and col1 <= col <= col2

    def getValue(self, row: int, col: int) -> int:
        for op in self.ops[::-1]:
            if self.is_in_rect(row, col, op[0], op[1], op[2], op[3]):
                return op[4]
        return self.rect[row][col]



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
