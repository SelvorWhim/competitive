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
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        return isValidBstRecursive(root->left, 0, false, root->val, true) && isValidBstRecursive(root->right, root->val, true, 0, false);
    }
    bool isValidBstRecursive(TreeNode* node, int min, bool has_min, int max, bool has_max) {
        if (node == nullptr) {
            return true;
        }
        if ((has_min && node->val <= min) || (has_max && node->val >= max)) {
            // note: based on examples, equal values are not allowed, otherwise it would be strict inequality
            return false;
        }
        return isValidBstRecursive(node->left, min, has_min, node->val, true) && isValidBstRecursive(node->right, node->val, true, max, has_max);
    }
};
