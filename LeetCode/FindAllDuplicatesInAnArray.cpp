/*
constant extra space you say? (besides the output, presumably, but that may have size <<n) alright, let's get hacky and use the given array
the given ints are positive, but the data type allows negatives, so we can flip a number's sign to store extra information
namely, nums[i] will be negative if we've seen i+1 before (since number range is 1-n and index range is 0-(n-1))
*/

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ret;
        for (int x: nums) {
            if (x < 0) {
                x = 0 - x;
            }
            if (nums[x-1] < 0) { // has already been flipped, so it appears twice
                ret.push_back(x);
            }
            else {
                nums[x-1] = 0 - nums[x-1];
            }
        }
        return ret;
    }
};
