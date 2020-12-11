class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        int last_val = nums[0];
        int last_val_i = 0;
        bool is_second = false;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != last_val) {
                nums[++last_val_i] = nums[i];
                last_val = nums[i];
                is_second = false;
            }
            else if (!is_second) {
                nums[++last_val_i] = nums[i];
                is_second = true;
            }
        }
        return last_val_i + 1;
    }
};
