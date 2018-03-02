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
        # validate rows and columns
        for i in range(9):
            sr = set() # seen set for row being validated
            sc = set() # seen set for column being validated
            for j in range(9):
                if not validCell(board[i][j], sr):
                    return False
                if not validCell(board[j][i], sc):
                    return False
        # validate (relevant) 3x3 blocks
        for i in range(3):
            for j in range(3):
                sb = set() # seen set for block being validated
                for k in range(3):
                    for l in range(3): # never thought I'd have reason to use a 4-level loop (on an object of depth less than 4), yet here I am. It could have been 2 levels but this is more convenient
                        if not validCell(board[i*3+k][j*3+l], sb):
                            return False
        return True
