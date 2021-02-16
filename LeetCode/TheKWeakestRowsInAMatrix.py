class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # could be made more efficient with heaps but this is the simple solution
        return [i for (i,row) in sorted(enumerate(mat), key=lambda x: (x[1],x[0]))][:k]
