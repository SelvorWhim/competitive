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
    bool isBalanced(TreeNode* root) {
        int unused;
        return isBalancedHeight(root, &unused);
    }
    
    bool isBalancedHeight(TreeNode* root, int* height) {
        if (root == nullptr) {
            height = 0;
            return true;
        }
        int left_h = 0;
        int right_h = 0;
        bool ret = isBalancedHeight(root->left, &left_h) && isBalancedHeight(root->right, &right_h)
                    && std::abs(left_h-right_h) <= 1;
        *height = std::max(left_h, right_h) + 1;
        return ret;
    }
};
