#include <algorithm>

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
        
    int maxAncestorDiffInner(TreeNode* root, int min_ancestor, int max_ancestor) {
        min_ancestor = std::min(min_ancestor, root->val);
        max_ancestor = std::max(max_ancestor, root->val);
        int left_diff = (root->left != nullptr) ? maxAncestorDiffInner(root->left, min_ancestor, max_ancestor) : 0;
        int right_diff = (root->right != nullptr) ? maxAncestorDiffInner(root->right, min_ancestor, max_ancestor) : 0;
        return std::max(std::max(left_diff, right_diff), std::max(std::abs(max_ancestor-root->val), std::abs(min_ancestor-root->val)));
    }
};
