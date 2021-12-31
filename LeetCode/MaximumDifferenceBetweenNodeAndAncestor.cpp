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
    int maxAncestorDiff(TreeNode* root) {
        return maxAncestorDiffInner(root, root->val, root->val);
    }
    
    int maxAncestorDiffInner(TreeNode* node, int min_ancestor, int max_ancestor) {
        if (node == nullptr) {
            return 0;
        }
        min_ancestor = min(min_ancestor, node->val);
        max_ancestor = max(max_ancestor, node->val);
        int left_max_diff = maxAncestorDiffInner(node->left, min_ancestor, max_ancestor);
        int right_max_diff = maxAncestorDiffInner(node->right, min_ancestor, max_ancestor);
        return max(max(max_ancestor - node->val, node->val - min_ancestor), max(left_max_diff, right_max_diff));
    }
};