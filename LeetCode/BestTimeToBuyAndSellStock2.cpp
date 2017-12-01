class Solution {
public:
    // idea: in this version, it's worth buying/selling whenever there's a rise.
    // for simplicity, I act as though we can re-buy what we just sold - since only total profit is asked, buying 1 and selling at 2 then buying 2 and selling at 3 is equivalent to buying at 1 and selling at 3.
	// when there's a rise, always sell what you bought. When there's a fall, retroactively replace what you bought with the cheaper version.
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) return 0;
        int profit = 0;
        int bought = prices[0];
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] > bought) {
                profit += prices[i] - bought;
            }
            bought = prices[i];
        }
        return profit;
    }
};
