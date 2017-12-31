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
    int sumOfLeftLeaves(TreeNode* root) {
        return sumOfLeftLeaves(root, false); // unspecified case: what if the tree is a single leaf? If that counts as a left leaf, change this false to true. // note: tested on site and this version works while true doesn't, so a single leaf is not a left leaf.
    }
    
    int sumOfLeftLeaves(TreeNode* root, bool isLeftBranch) {
        if (root == NULL) {
            return 0;
        }
        if (isLeftBranch && root -> left == NULL && root -> right == NULL) { // is left leaf
            return root->val;
        }
        return sumOfLeftLeaves(root->left, true) + sumOfLeftLeaves(root->right, false);
    }
};
