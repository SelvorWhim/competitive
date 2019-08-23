// linear space and time version
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> found; // maps each value to last index where it's been found before
        for (int i = 0; i < nums.size(); i++) {
            int curr = nums[i];
            if (found.find(target - curr) != found.end()) {
                return vector<int> {found[target-curr], i};
            }
            found[curr] = i;
        }
        return vector<int> {-1,-1}; // shouldn't happen based on assumptions
    }
};
