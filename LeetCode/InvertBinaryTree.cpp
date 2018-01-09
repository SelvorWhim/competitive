// this implementation changes the original tree, rather than making a new one with copies of the nodes

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
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) return NULL;
        TreeNode* invLeft = invertTree(root->left);
        TreeNode* invRight = invertTree(root->right);
        root->right = invLeft;
        root->left = invRight;
        return root;
    }
};
