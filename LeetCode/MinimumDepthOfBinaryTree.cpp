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
    int minDepth(TreeNode* root) {
        if (root == NULL) return 0; // based on examples, answer for empty tree is 0. For convenient recursion, separate this case...
        return minDepth1(root);
    }
    
    int minDepth1(TreeNode* root) {
        if (root == NULL) return INT_MAX;
        if (root -> left == NULL && root -> right == NULL) return 1;
        return 1 + min(minDepth1(root->left), minDepth1(root->right));
    }
};
