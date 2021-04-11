# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveDeepestLeavesSum(self, node: TreeNode, currLevel: int):
        if node is None:
            return
        if node.left is None and node.right is None:
            if currLevel > self.deepestLevel:
                self.deepestSum = node.val
            elif currLevel == self.deepestLevel:
                self.deepestSum += node.val
            self.deepestLevel = max(self.deepestLevel, currLevel)
            if currLevel > self.deepestLevel: # shallow leaf
                return
        self.recursiveDeepestLeavesSum(node.left, currLevel+1)
        self.recursiveDeepestLeavesSum(node.right, currLevel+1)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.deepestLevel = 0
        self.deepestSum = 0
        self.recursiveDeepestLeavesSum(root, 0)
        return self.deepestSum
