// idea: find sum first, go through again to see where the sum on the left becomes equal to the right according to total sum.
// there must be a more optimal way with iteration from both sides, but I doubt there's anything asymptotically better.

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sumAll = 0;
        for (auto& x : nums) sumAll += x;
        int sumLeft = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (sumLeft == sumAll - (sumLeft + nums[i])) { // if sum on the left is eaual to sum on the right
                return i;
            }
            sumLeft += nums[i];
        }
        return -1;
    }
};
