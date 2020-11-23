# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dp = {}
    def rob(self, root: TreeNode, can_pick_root: bool = True) -> int:
        if root == None:
            return 0
        # use memoization to prevent exponential growth
        if (root, can_pick_root) in self.dp:
            return self.dp[(root, can_pick_root)]
        with_root = root.val + self.rob(root.left, False) + self.rob(root.right, False) if can_pick_root else 0
        without_root = self.rob(root.left, True) + self.rob(root.right, True)
        ret = max(with_root, without_root)
        self.dp[(root, can_pick_root)] = ret # memoize
        return ret
