# assumption: board is of valid size, and contains only single character strings with digits or '.'

def validCell(val, seen):
    if val != '.' and val in seen:
        return False
    else:
        seen.add(val)
        return True

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9): # row/column/block index
            sr = set() # seen set for row being validated
            sc = set() # seen set for column being validated
            sb = set() # seen set for 3x3 block being validated
            for j in range(9): # index within row/column/block
                if not validCell(board[i][j], sr):
                    return False
                if not validCell(board[j][i], sc):
                    return False
                if not validCell(board[3*(i//3) + (j//3)][3*(i%3) + (j%3)], sb): # translation of block index / in-block index to row/column indexes
                    return False
        return True
