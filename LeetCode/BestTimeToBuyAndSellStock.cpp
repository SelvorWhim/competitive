class Solution {
public:
	// idea: iterate backwards over prices, remember what the maximum sell price is later and so find the maximum profit if the buying price is the current. Keep track of the max of these values, giving maximum profit over the list.
	
	/*
    // non-optimized v1 - O(n) time, O(n) space. Pretty sure I can change it to use constant extra space.
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
	*/
	
	/*
	// non-optimized v2 - same complexity, shorter with joined loops
	int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        int maxAfter[n];
        maxAfter[n-1] = 0;
        int maxProfit = 0;
        for (int i = n-2; i >= 0; i--) {
            maxAfter[i] = max(maxAfter[i+1], prices[i+1]);
            maxProfit = max(maxProfit, maxAfter[i] - prices[i]);
        }
        return maxProfit;
    }
	*/
	
	// optimized version - O(n) time, O(1) space
	int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) return 0;
        int maxAfterNext = 0;
        int maxProfit = 0;
        for (int i = prices.size()-2; i >= 0; i--) {
            maxAfterNext = max(maxAfterNext, prices[i+1]);
            maxProfit = max(maxProfit, maxAfterNext - prices[i]);
        }
        return maxProfit;
    }
};
