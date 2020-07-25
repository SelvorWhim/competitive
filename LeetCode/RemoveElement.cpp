class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int lf = -1; // last free spot
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == val && (lf == -1)) {
                lf = i;
            }
            else if (nums[i] != val && (lf != -1)) {
                nums[lf] = nums[i];
                lf++;
            }
        }
        if (lf == -1) {
            return nums.size(); // none were val
        }
        return lf;
    }
};
