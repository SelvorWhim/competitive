// idea: because BST, if the root is outside a boundary, one of its branches will necessarily be outside the same boundary
// (and the new root will be the start of the other branch, or something further down that branch - the trimmed version of ONE subtree)
// thus, a recursive solution is relatively simple

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
    // this implementation is recursive, and modifies the original tree
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        if (root == NULL) return NULL;
        if (root->val < L) return trimBST(root->right, L, R); // too small, so left subtree will be too small
        if (root->val > R) return trimBST(root->left, L, R); // too small, so right subtree will be too small
        root->left = trimBST(root->left, L, R);
        root->right = trimBST(root->right, L, R);
        return root;
    }
};
