class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> ret;
        long long running_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            running_sum += nums[i];
            ret.push_back(running_sum);
        }
        return ret;
    }
};
