// we can't know if where the deepest path might be in the tree, need to search the whole tree. If the search is left to right (either dfs or bfs, as long as left children are searched before right), the simplest way is to update a bottom-left value iff a deeper layer is reached than before.
// this implementation is stateful

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
private:
    int deepest = -1; // updated whenever we reach a deeper row
    int blVal; // updated whenever we reach a deeper row in a left-to-right search
public:
    int findBottomLeftValue(TreeNode* root) {
        deepest = -1;
        searchBottomLeftValue(root, 0);
        return blVal;
    }
    
    void searchBottomLeftValue(TreeNode* root, int depth) {
        if (root == NULL) return;
        if (depth > deepest) {
            deepest = depth;
            blVal = root->val;
        }
        searchBottomLeftValue(root->left, depth + 1);
        searchBottomLeftValue(root->right, depth + 1);
    }
};
