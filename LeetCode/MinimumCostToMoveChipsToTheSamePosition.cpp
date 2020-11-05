// takes 0 cost to move chips to the same parity (multiple steps), and 1 to switch parity
// so just count how many in each parity of positions, and return the minimum

class Solution {
public:
    int minCostToMoveChips(vector<int>& positions) {
        int num_evens = 0;
        int num_odds = 0;
        for (int position : positions) {
            if (position % 2 == 0) {
                num_evens++;
            }
            else {
                num_odds++;
            }
        }
        return min(num_evens, num_odds);
    }
};
