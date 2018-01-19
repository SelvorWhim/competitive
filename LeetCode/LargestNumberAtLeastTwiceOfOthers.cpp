// idea: find largest number (keep its index) and second largest, check if one is at least twice as big as the other.

class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        if (nums.size() == 1) {
            return 0; // based on test result, list of length 1 should return 0 (biggest number is twice as big by default)
        }
        int i_1 = 0, i_2 = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i_1]) {
                i_2 = i_1;
                i_1 = i;
            } else if (nums[i] > nums[i_2]) {
                i_2 = i;
            }
        }
        if (nums[i_1] >= 2*nums[i_2]) { 
            return i_1;
        } else {
            return -1;
        }
    }
};
