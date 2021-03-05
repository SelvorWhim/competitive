# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.level_to_sum = Counter()
        self.level_to_count = Counter()
        self.averageOfLevelsRecursion(root, 0)
        height = len(self.level_to_sum)
        level_avgs = [self.level_to_sum[i]/self.level_to_count[i] for i in range(height)]
        return level_avgs
    
    def averageOfLevelsRecursion(self, root: TreeNode, level: int) -> None:
        if root is None:
            return
        self.level_to_sum[level] += root.val
        self.level_to_count[level] += 1
        self.averageOfLevelsRecursion(root.left, level+1)
        self.averageOfLevelsRecursion(root.right, level+1)
