/*
// idea: since all houses contain non-negative amounts,
// at each step the thief needs to choose whether to skip 1 house or 2
// (skipping 0 would trigger the alarm, and skipping 3+ means he could've robbed an extra house in the middle)
// similarly, needs to choose whether to start at the 1st or 2nd house
// there's a subproblem structure that fits dynamic programming well
// storing the maximum value when starting from the ith house (1d array) allows calculating backwards from the end
*/

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        
        if (n == 0) return 0;
        if (n <= 2) return max(nums[0], nums[n-1]); // works for n=1 and n=2
        
        int substreet_max[n];
        
        // initialize: possible houses to end with
        substreet_max[n-1] = nums[n-1];
        substreet_max[n-2] = max(nums[n-2], nums[n-1]);
        
        // calculate subproblems: substreet_max[i] = maximum amount thief can rob starting from house i
        for (int i = n-3; i >= 0; i--) {
            substreet_max[i] = max(nums[i] + substreet_max[i+2], substreet_max[i+1]); // 1st case: rob house i, 2nd case: skip it and get the most starting from the next house
        }
        
        return substreet_max[0];
    }
};
