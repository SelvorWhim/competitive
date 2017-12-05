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
	// recursive solution
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (root == NULL) return ret;
        ret = inorderTraversal(root->left);
        ret.push_back(root->val);
        vector<int> ret_r = inorderTraversal(root->right);
        ret.insert(ret.end(), ret_r.begin(), ret_r.end());
        return ret;
    }
};
