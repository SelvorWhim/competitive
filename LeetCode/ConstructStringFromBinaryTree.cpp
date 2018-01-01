// based on the examples, leaves should not have children indicated by empty parentheses, and a missing right child should not be indicated by empty parentheses (but a missing left child should).

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
    string tree2str(TreeNode* t) {
        if (t == NULL) return ""; // empty tree - either the whole tree is empty or this is the left child of a node with a right child
        if (t->right == NULL) { // no right child - leaf / left branch (by condition)
            return to_string(t->val)
                + ((t->left == NULL) ? "" : ("(" + tree2str(t->left) + ")"));
        } else { // right branch / both branches
            return to_string(t->val)
                + "(" + tree2str(t->left) + ")"
                + "(" + tree2str(t->right) + ")";
        }
    }
    
    
};
