class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        bool found_violation = false;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < nums[i-1]) {
                if (found_violation) {
                    // 2nd case of decreasing, can't be fixed by changing one element
                    return false;
                }
                if (i > 1 && i + 1 < nums.size() && nums[i-2] > nums[i] && nums[i-1] > nums[i+1]) {
                    // any violation by an edge can be fixed
                    // and any in the middle can be fixed by setting nums[i-1] = nums[i-2] or nums[i] = nums[i-1]
                    // anything else (this case) can't be fixed
                    return false;
                }
                found_violation = true;
            }
        }
        return true;
    }
};
