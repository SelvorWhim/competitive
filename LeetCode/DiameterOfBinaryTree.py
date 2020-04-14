# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeHeight(self, root: TreeNode) -> int:
        """
        updates max diameter for subtree and returns its height
        height such that height(None) = 0
        """
        if root == None:
            return 0
        left_height = self.treeHeight(root.left)
        right_height = self.treeHeight(root.right)
        self.max_diameter = max(self.max_diameter, left_height + right_height)
        return max(left_height, right_height) + 1
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0
        self.treeHeight(root)
        return self.max_diameter
