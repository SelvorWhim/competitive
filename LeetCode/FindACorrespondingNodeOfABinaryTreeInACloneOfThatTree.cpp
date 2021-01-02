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
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        TreeNode* ret;
        if (original == nullptr) {
            return nullptr;
        }
        if (original == target) { // this way it works even with non-unique values
            return cloned;
        }
        ret = getTargetCopy(original->left, cloned->left, target);
        if (ret == nullptr) {
            ret = getTargetCopy(original->right, cloned->right, target);
        }
        return ret;
    }
};
