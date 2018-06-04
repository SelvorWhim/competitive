class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[cell^1 for cell in row][::-1] for row in A] # ^1 (XOR with 1) inverts cells containing 0/1
