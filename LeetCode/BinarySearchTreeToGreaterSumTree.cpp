// note: with function name changed to convertBST, also works for Convert BST to Greater Tree

/*
idea: iterate the tree inorder but right to left (that gives decreasing order in a BST),
keep a running sum of the original nodes, add the running sum to each node
*/

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
private:
    int sum_so_far = 0;
public:
    TreeNode* bstToGst(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        (void)bstToGst(root->right);
        int greater_sum = this->sum_so_far;
        this->sum_so_far += root->val;
        root->val += greater_sum;
        (void)bstToGst(root->left);
        return root;
    }
};
