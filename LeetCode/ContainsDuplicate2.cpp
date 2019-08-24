class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k <= 0) {
            return false;
        }
        unordered_set<int> seen;
        for (int i = 0; i < nums.size(); i++) {
            if (i-k >= 1) {
                seen.erase(nums[i-k-1]);
            }
            if (seen.find(nums[i]) == seen.end()) {
                seen.insert(nums[i]);
            }
            else {
                return true;
            }
        }
        return false;
    }
};
