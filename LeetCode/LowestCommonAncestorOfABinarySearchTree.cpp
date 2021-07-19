// LCA in BST will have a value somewhere between p and q, so search for the range till you're between them

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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p == q) {
            return p;
        }
        if (p->val > q->val) {
            // switch them so I can assume p.val <= q.val
            TreeNode* temp = p;
            p = q;
            q = temp;
        }
        TreeNode* it = root;
        while (it != NULL) {
            if (it->val > q->val) {
                it = it->left;
            }
            else if (it->val < p->val) {
                it = it->right;
            }
            else {
                return it;
            }
        }
        return NULL; // this shouldn't happen
    }
};
