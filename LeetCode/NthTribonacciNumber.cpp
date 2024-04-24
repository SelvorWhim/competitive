// Constraints say n <= 37 so we don't need to work out a direct formula, iterative approach is the simplest and fast enough.

class Solution {
public:
    int tribonacci(int n) {
        int last_three[3] = {0, 1, 1};
        if (n < 3) {
            return last_three[n];
        }
        for (int i = 3; i < n; i++) {
            int sum = last_three[0] + last_three[1] + last_three[2];
            last_three[0] = last_three[1];
            last_three[1] = last_three[2];
            last_three[2] = sum;
        }
        return last_three[0] + last_three[1] + last_three[2];
    }
};
