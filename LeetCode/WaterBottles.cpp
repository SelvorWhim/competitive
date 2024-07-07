// there's probably a closed formula for this, but it's easy to get off-by-1 with it and
// the iterative version is only log(numBottles)(base numExchange), fast enough given the constraints

class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int drunkBottles = 0;
        int fullBottles = numBottles;
        int emptyBottles = 0;
        while (fullBottles > 0) {
            // drink all the full bottles
            drunkBottles += fullBottles;
            emptyBottles += fullBottles;
            // skip implied fullBottles = 0 since we're setting it right after
            fullBottles = emptyBottles / numExchange;
            emptyBottles = emptyBottles % numExchange;
        }
        return drunkBottles;
    }
};
