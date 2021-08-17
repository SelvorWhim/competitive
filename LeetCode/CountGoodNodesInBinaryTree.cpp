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
public:
    int goodNodes(TreeNode* root) {
        return goodNodesRecursion(root, root->val);
    }
    
    int goodNodesRecursion(TreeNode* root, int max_so_far) {
        if (root == nullptr) {
            return 0;
        }
        int curr_good = max_so_far > root->val ? 0 : 1;
        max_so_far = std::max(max_so_far, root->val);
        return curr_good + goodNodesRecursion(root->left, max_so_far) + goodNodesRecursion(root->right, max_so_far);
    }
};
