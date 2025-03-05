# past k=1, on minute k, 4(k-1) squares are added
# so we have a simple arithmetic sum for which there's a closed formula

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2*n*(n-1)
