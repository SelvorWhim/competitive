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
    TreeNode* it;
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* pre_root = new TreeNode(); // dummy node, its next will be the answer
        this->it = pre_root;
        increasingBstRecursion(root);
        return pre_root->right;
    }
    void increasingBstRecursion(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        increasingBstRecursion(root->left);
        this->it->right = new TreeNode(root->val);
        this->it = it->right;
        increasingBstRecursion(root->right);
    }
};
