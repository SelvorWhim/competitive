class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        for i in range(n):
            row = m*[0]
            for j in range(m):
                row[j] = matrix[j][i]
            ret.append(row)
        return ret
