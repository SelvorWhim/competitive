class Solution {
public:
    // it's a base 26 positional counting system, basically
	// original signature used int but that's too short for max input
    long titleToNumber(string s) {
        long sum = 0;
        long base = 26;
        long factor = 1;
        for (int i = s.length() - 1; i >= 0; i--) {
            int letterVal = s[i] - 'A' + 1;
            sum += factor * letterVal;
            factor *= base;
        }
        return sum;
    }
};
