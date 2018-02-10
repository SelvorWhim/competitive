// idea: variant of binary search - need first index where number is equal or greater than target.
// Pretty sure all the variants are implemented in the standard library, but this is an implementation from scratch.
// As a result of a series of patches for a fiddly problem this code is pretty ugly, but it works

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int lo = 0;
        int hi = nums.size() - 1;
        int mid = 0;
        while (lo < hi) {
            mid = lo + (hi-lo)/2;
            if (nums[mid] == target) {
                return mid;
            } else {
                if (lo == mid || hi == mid) {
                    if (nums[mid] < target) mid++;
                    break;
                }
                if (nums[mid] < target) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }
        }
        if (nums[mid] < target) {
            return mid + 1;
        } else {
            return mid;
        }
    }
};
