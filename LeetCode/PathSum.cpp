/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL) { // make sure it doesn't return true for partial paths because of nodes with single children
            return false;
        }
        if (root->left == NULL && root->right == NULL) { // leaf
            return (sum == root->val);
        }
        int sumRemnant = sum - root->val;
        return (hasPathSum(root->left, sumRemnant) || hasPathSum(root->right, sumRemnant));
    }
};
