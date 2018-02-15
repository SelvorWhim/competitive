// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int lo = 1;
        int hi = n;
        while (lo < hi) {
            int g = lo + (hi-lo)/2;
            int r = guess(g);
            if (r == 0) {
                return g;
            } else if (r < 0) {
                hi = g - 1;
            } else {
                lo = g + 1;
            }
        }
        return lo;
    }
};
