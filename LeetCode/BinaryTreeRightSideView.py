# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.right_view = []
        self.rightSideViewRecursive(root, 0)
        return self.right_view
        
    def rightSideViewRecursive(self, root: TreeNode, depth: int) -> None:
        if root is None:
            return
        if len(self.right_view) > depth:
            self.right_view[depth] = root.val
        else:
            self.right_view.append(root.val)
        self.rightSideViewRecursive(root.left, depth+1) # left side must be updated first
        self.rightSideViewRecursive(root.right, depth+1) # then right overrides it if it reaches down far enough
