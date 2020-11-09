# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.maxAncestorDiffInner(root, root.val, root.val)
    
    def maxAncestorDiffInner(self, root: TreeNode, min_ancestor: int, max_ancestor: int) -> int:
        min_ancestor = min(min_ancestor, root.val)
        max_ancestor = max(max_ancestor, root.val)
        left_diff = self.maxAncestorDiffInner(root.left, min_ancestor, max_ancestor) if root.left is not None else 0
        right_diff = self.maxAncestorDiffInner(root.right, min_ancestor, max_ancestor) if root.right is not None else 0
        return max(left_diff, right_diff, abs(max_ancestor-root.val), abs(min_ancestor-root.val))
