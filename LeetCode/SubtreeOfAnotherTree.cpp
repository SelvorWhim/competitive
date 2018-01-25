// idea: for every node of s, check if the subtree rooted at the node is identical to t.
// complexity: most nodes will be ruled out within a level or two, so in most cases complexity should be O(n) (for n nodes), the only problem is if both trees contains a lot of identical values, in which case in might be O(n^2).

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
    // (copied from my solution to "Same Tree" problem)
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL) return true;
        if (p == NULL || q == NULL) return false; // following previous, one but not the other
        return (p->val == q->val) && (isSameTree(p->left, q->left)) && (isSameTree(p->right, q->right));
    }
    
    // s is main tree, t is potential subtree
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (isSameTree(s,t)) return true;
        if (s == NULL || t == NULL) return false; // following previous, one but not the other
        return (isSubtree(s->left,t) || isSubtree(s->right,t));
    }
};
