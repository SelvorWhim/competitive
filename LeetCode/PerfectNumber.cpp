class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false; // 0,1 are special cases that would make other conditions messy
        int sum = 0;
        double sq = sqrt(num);
        for (int i = 1; i <= sq; i++) {
            if (num % i == 0) {
                sum += i;
                if (i > 1 && i < sq) {
                    sum += (num/i); // anything other than an actual square root will only appear once in this limited iteration
                }
                if (sum > num) {
                    return false;
                }
            }
        }
        if (sum == num) {
            return true;
        } else {
            return false;
        }
    }
};
