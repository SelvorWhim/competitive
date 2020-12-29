# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter

# counter represents a pseudo-palindrome path if there's at most one odd count
def counter_is_pseudo_palilndrome(counter: Counter):
    odd_found = False
    for count in counter.values():
        if count % 2 == 1:
            if odd_found:
                return False
            odd_found = True
    return True

class Solution:
    paths_found = 0
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.paths_found = 0
        counter = Counter()
        self.pseudoPalindromicPathsRecursive(root, counter)
        return self.paths_found
        
    def pseudoPalindromicPathsRecursive(self, node: TreeNode, counter: Counter) -> int:
        if node is None:
            return
        counter[node.val] += 1
        if node.left is None and node.right is None:
            if counter_is_pseudo_palilndrome(counter):
                print(counter)
                self.paths_found += 1
        else:
            self.pseudoPalindromicPathsRecursive(node.left, counter)
            self.pseudoPalindromicPathsRecursive(node.right, counter)
        counter[node.val] -= 1
