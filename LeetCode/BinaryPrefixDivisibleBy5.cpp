/*
going from shorter numbers to longer, you multiply by 2 then add the last digit
do the multiplication and addition in mod 5
to know whether the current number is divisible by 5 without recalculating
*/

class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& A) {
        int N_i_mod5 = 0;
        vector<bool> ret;
        for (int b: A) {
            N_i_mod5 *= 2;
            N_i_mod5 += b;
            N_i_mod5 %= 5; // TIL %= is a thing
            ret.push_back(N_i_mod5 == 0);
        }
        return ret;
    }
};
