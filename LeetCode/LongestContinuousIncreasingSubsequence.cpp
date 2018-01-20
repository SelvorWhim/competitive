// continuous subsequences are much easier to check than all subsequences
// based on examples, we're looking for STRICTLY increasing subsequences

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.size() < 1) return 0;
        int maxRun = 1;
        int run = 1;
        int last = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > last) {
                run++;
            } else {
                maxRun = max(run, maxRun);
                run = 1;
            }
            last = nums[i];
        }
        maxRun = max(run, maxRun);
        return maxRun;
    }
};
