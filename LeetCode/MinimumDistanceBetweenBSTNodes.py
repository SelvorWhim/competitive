# inorder traversal in BST gives the nodes in order, so scan it that way

MAX_VAL = 100000  # problem constrains tree values to [0, 10^5]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def updateMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.updateMinimumDifference(root.left)
        # don't even neeed abs() if we're going in order
        self.min_diff = min(self.min_diff, root.val - self.prev_val)
        self.prev_val = root.val
        self.updateMinimumDifference(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev_val = -MAX_VAL
        self.min_diff = MAX_VAL
        self.updateMinimumDifference(root)
        return self.min_diff
