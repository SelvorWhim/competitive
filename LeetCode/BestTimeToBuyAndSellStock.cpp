class Solution {
public:
    // non-optimized version - O(n) time, O(n) space. Pretty sure I can change it to use constant extra space.
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        int maxAfter[n-1];
        maxAfter[n-2] = prices[n-1];
        for (int i = n-3; i >= 0; i--) {
            maxAfter[i] = max(maxAfter[i+1], prices[i+1]);
        }
        int maxProfit = 0;
        for (int i = 0; i < n-1; i++) {
            int profit = maxAfter[i] - prices[i];
            if (profit > maxProfit)
                maxProfit = profit;
        }
        return maxProfit;
    }
};
