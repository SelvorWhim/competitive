# assumption: board is of valid size, and contains only single character strings with digits or '.'

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
                curr = board[i][j]
                if curr != '.' and curr in sr:
                    return False
                else:
                    sr.add(curr)
                curr = board[j][i]
                if curr != '.' and curr in sc:
                    return False
                else:
                    sc.add(curr)
        # validate (relevant) 3x3 blocks
        for i in range(3):
            for j in range(3):
                sb = set() # seen set for block being validated
                for k in range(3):
                    for l in range(3): # never thought I'd have reason to use a 4-level loop (on an object of depth less than 4), yet here I am. It could have been 2 levels but this is more convenient
                        curr = board[i*3+k][j*3+l]
                        if curr != '.' and curr in sb:
                            return False
                        else:
                            sb.add(curr)
        return True
