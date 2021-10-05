class Solution {
public:
    // dynamic programming solution - O(n) time, O(n) space
	// (non-optimal, as it turns out, since the problem can be reduced to the fibonacci sequence for which there is a closed formula for this, but it was accepted)
    int climbStairs(int n) {
        vector<int> counts {1,1}; // 1 way to split a 1, and 1 way to split a 0 just to provide a base case that works with the rest (if n is positive, it won't come up in and of itself)
        for (int i = 2; i <= n; i++) {
            counts.push_back(counts[i-2] + counts[i-1]);
        }
        return counts[n];
    }
};
