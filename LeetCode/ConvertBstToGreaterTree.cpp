// idea: reverse inorder traversal will order elements from greatest to smallest in BST, so we can have a runing sum to add to the current element for the desired modification
// in-place, stateful implementation (O(1) extra space, but original tree is altered)

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
private:
    int sumSoFar = 0; // sum of stuff that's bigger than node currently being worked on in the original tree
public:
    TreeNode* convertBST(TreeNode* root) {
        if (root == NULL) return NULL;
        convertBST(root->right);
        root->val += sumSoFar;
        sumSoFar = root->val;
        convertBST(root->left);
        return root;
    }
};
