# each index inverts the parity of the row and the column
# We can keep the parities of rows and columns updated, then calculate the parities of each 2D point based on them
# and the number of odd points is the number of odd columns * number of odd rows
# space: O(n+m)

# wait, no, that's just wrong, see after one step in the example

# TODO: optimize to not initialize when not necessary
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row_odd = {i:False for i in range(n)}
        col_odd = {j:False for j in range(m)}
        
        for i,j in indices:
            row_odd[i] = not row_odd[i]
            col_odd[j] = not col_odd[j]
        print(row_odd)
        print(col_odd)
        return sum(row_odd.values()) * sum(col_odd.values())
