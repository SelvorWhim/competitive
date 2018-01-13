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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<long> levelSums;
        vector<long> levelCount;
        sumLevels(root, 0, 0, levelSums, levelCount);
        int levelN = levelCount.size();
        vector<double> levelAvgs = vector<double>(levelN);
        for (int i = 0; i < levelN; i++) {
            levelAvgs[i] = (double)levelSums[i] / levelCount[i];
        }
        return levelAvgs;
    }
    
    // return value is the number of levels reached so far (not necessarily complete), for convenience
    void sumLevels(TreeNode* currNode, int currLevel, int levelsReached, vector<long>& levelSums, vector<long>& levelCount) {
        if (currNode == NULL) return;
        if (currLevel >= levelsReached) { // should be at most greater by 1
            levelSums.push_back(0);
            levelCount.push_back(0);
        }
        levelCount[currLevel]++;
        levelSums[currLevel] += currNode->val;
        sumLevels(currNode->left, currLevel + 1, levelSums.size(), levelSums, levelCount);
        sumLevels(currNode->right, currLevel + 1, levelSums.size(), levelSums, levelCount);
    }
};
