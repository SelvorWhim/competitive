# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePathsUtil(self, root: Optional[TreeNode], path_so_far: List[int]) -> List[str]:
        if not root:
            return
        path_so_far.append(root.val)
        if not root.left and not root.right:
            self.paths.append("->".join(str(n) for n in path_so_far))
        self.binaryTreePathsUtil(root.left, path_so_far)
        self.binaryTreePathsUtil(root.right, path_so_far)
        del path_so_far[-1]


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        self.binaryTreePathsUtil(root, [])
        return self.paths
