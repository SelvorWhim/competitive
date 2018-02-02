// idea: iterate through both sides of the tree in parallel, symmetrically, until a mismatch is found or whole tree is checked

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
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        return areReflections(root->left, root->right);
    }
    
    bool areReflections(TreeNode* t1, TreeNode* t2) {
        if (t1 == NULL && t2 == NULL) return true;
        if (t1 == NULL || t2 == NULL) return false; // one but not the other
        if (t1->val != t2->val) return false;
        return areReflections(t1->left, t2->right) && areReflections(t1->right, t2->left);
    }
};
