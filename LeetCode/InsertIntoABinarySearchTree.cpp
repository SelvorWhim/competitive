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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* curr = root;
        while (curr != nullptr) {
            if (val < curr->val) {
                if (curr->left == nullptr) {
                    curr->left = new TreeNode(val);
                    return root;
                }
                else {
                    curr = curr->left;
                }
            }
            else {
                if (curr->right == nullptr) {
                    curr->right = new TreeNode(val);
                    return root;
                }
                else {
                    curr = curr->right;
                }
            }
        }
        return new TreeNode(val); // this should only happen if original root was null
    }
};
