class Solution {
public:
    # it's a base 26 positional counting system, basically
    int titleToNumber(string s) {
        int sum = 0;
        int base = 26;
        int factor = 1;
        for (int i = s.length() - 1; i >= 0; i--) {
            int letterVal = s[i] - 'A' + 1;
            sum += factor * letterVal;
            factor *= base;
        }
        return sum;
    }
};
