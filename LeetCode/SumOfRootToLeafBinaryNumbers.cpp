/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumRootToLeaf(TreeNode* curr, int sum_so_far) {
        if (curr == nullptr) {
            return 0;
        }
        int sum_for_lower = sum_so_far * 2 + curr->val;
        if (curr->left == nullptr && curr->right == nullptr) {
            return sum_for_lower;
        }
        else {
            return sumRootToLeaf(curr->left, sum_for_lower) + sumRootToLeaf(curr->right, sum_for_lower);
        }
    }
    
    int sumRootToLeaf(TreeNode* root) {
        return sumRootToLeaf(root, 0);
    }
    
};
