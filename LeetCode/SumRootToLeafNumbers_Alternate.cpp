// NOTE: I read too quickly and misunderstood the question. My implementation sums the sums of all root-to-leaf paths numerically, not the string sums created by treating the nodes as characters, as was defined. I found no problem on the site that's like what I assumed, so the code is untested, but maybe it'll be useful somewhere.

// idea: since we're summing all and not distinguishing between individual paths, each number will appear in the total sum potentially multiple times equal to the number of leaves in its subtree, including itself

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
    int totalSum;
public:
    int sumNumbers(TreeNode* root) {
        totalSum = 0;
        countLeavesAndSum(root);
        return totalSum;
    }
    
    // returns leaf count in subtree (including itself), increments sum as side effect
    int countLeavesAndSum(TreeNode* root) {
        if (root == NULL) return 0;
        if (root->left == NULL && root->right == NULL) {
            totalSum += root->val;
            return 1;
        }
        int count = countLeavesAndSum(root->left) + countLeavesAndSum(root->right);
        totalSum += count * root->val;
        return count;
    }
};
