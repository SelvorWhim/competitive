class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        int last_val = nums[0];
        int last_val_i = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != last_val) {
                nums[last_val_i + 1] = nums[i];
                last_val = nums[i];
                last_val_i++;
            }
        }
        return last_val_i + 1;
    }
};
