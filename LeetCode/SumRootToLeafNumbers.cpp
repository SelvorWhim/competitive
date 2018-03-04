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
    int sumNumbers(TreeNode* root) {
        return sumSubtree(root, 0);
    }
    
    int sumSubtree(TreeNode* root, int sumSoFar) {
        if (root == NULL) return 0;
        int newSumSoFar = sumSoFar*10 + root->val;
        if (root->left == NULL && root->right == NULL) {
            return newSumSoFar;
        } else {
            return sumSubtree(root->left, newSumSoFar) + sumSubtree(root->right, newSumSoFar);
        }
    }
};
