// peaks are local, I doubt binary search would help here, gotta scan the whole thing. Beyond checking the edges first there's not much room for optimization.
// note: due to the specification on the edges, there will always be at least one peak.

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return n-1;
        if (nums[0] > nums[1]) return 0;
        if (nums[n-1] > nums[n-2]) return n-1;
        for (int i = 1; i < n-1; i++) {
            if (nums[i] > nums[i-1] && nums[i] > nums[i+1]) {
                return i;
            }
        }
        return -1; // this shouldn't happen
    }
};
