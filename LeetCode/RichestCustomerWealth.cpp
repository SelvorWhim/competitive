class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max_customer_wealth = 0; // as long as at least one of the customers has positive wealth (true under assumptions)
        for (vector<int> customer_accounts : accounts) {
            int customer_wealth = 0;
            for (int account : customer_accounts) {
                customer_wealth += account;
            }
            max_customer_wealth = max(max_customer_wealth, customer_wealth);
        }
        return max_customer_wealth;
    }
};
