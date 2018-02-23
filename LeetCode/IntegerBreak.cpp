// working upwards from small examples, the pattern seems to be to break into a sum with as many 3's as possible, except at the end where 4 = 2+2 is better than 4 = 3+1

class Solution {
public:
    int integerBreak(int n) {
        if (n <= 3) {
            return n-1;
        }
        if (n == 4) {
            return 4;
        }
        switch (n % 3) {
            case 0: return pow(3, n/3);
                     break;
            case 1: return pow(3, n/3 - 1) * 4;
                    break;
            case 2: return pow(3, n/3) * 2;
                    break;
        }
    }
};
