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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        int height; // unused except in recursion
        return subtreeWithAllDeepestRecursive(root, &height);
    }
    
    // height is output parameter
    TreeNode* subtreeWithAllDeepestRecursive(TreeNode* node, int* height) {
        if (node == nullptr) {
            *height = 0;
            return node;
        }
        int left_height, right_height;
        TreeNode* left_deepest_subtree = subtreeWithAllDeepestRecursive(node->left, &left_height);
        TreeNode* right_deepest_subtree = subtreeWithAllDeepestRecursive(node->right, &right_height);
        *height = std::max(left_height, right_height) + 1;
        if (left_height > right_height) {
            return left_deepest_subtree;
        }
        else if (left_height < right_height) {
            return right_deepest_subtree;
        }
        else {
            return node;
        }
    }
};
