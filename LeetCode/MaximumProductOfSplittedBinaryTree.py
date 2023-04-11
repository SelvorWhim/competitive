# first find the sum of the whole tree, then iterate over subtrees to find the one whose product with the remainder of the sum is maximal - O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sum_binary_tree(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return root.val + sum_binary_tree(root.left) + sum_binary_tree(root.right)

class Solution:
    def calculate_max_subtree_product(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        # calculate max subtree product for this subtree (set self.max_product_so_far as side effect), return sum of current subtree
        if not root:
            return 0
        curr_sum = root.val + self.calculate_max_subtree_product(root.left) + self.calculate_max_subtree_product(root.right)
        curr_product = (self.total_sum - curr_sum) * curr_sum
        self.max_product_so_far = max(curr_product, self.max_product_so_far)
        return curr_sum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.max_product_so_far = 0
        self.total_sum = sum_binary_tree(root)
        self.calculate_max_subtree_product(root)
        return self.max_product_so_far % 1000000007
