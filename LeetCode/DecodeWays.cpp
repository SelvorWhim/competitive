/**
 * letters are encoded as 1 or 2 digits
 * all 1-digit letters are possible except 0, and only some 2-digit letters are possible
 * so at every step, you must choose between decoding the current digit as is (unless it's a 0)
 * and decoding it together with the next digit (if that's a valid combination).
 * for each choice, sum the number of ways to decode the rest of the string
 * there will be lots of duplicate cases to consider (overlapping subproblems), so DP
 */

unsigned short char2digit(char c) {
     return c - '0';
}

class Solution {
private:
    int pairDecodings(unsigned short x1, unsigned short x2) {
        if (x1 == 0 || x1 > 2) {
            if (x2 == 0) {
                return -1; // illegal pair - whole string can't be decoded
            }
            return 0; // can't be decoded as pair, but string is still decodable (if first digit is taken alone)
        }
        if (x1 == 2 && x2 > 6) {
            return 0;
        }
        return 1;
    }
    int singleDecodings(unsigned short x) {
        return (x == 0) ? 0 : 1;
    }
public:
    // assumes all chars are valid digits
    int numDecodings(string s) {
        int n = s.size();
        int decodeFrom[n+1];
        decodeFrom[n] = 1; // to simplify edge case
        decodeFrom[n-1] = singleDecodings(char2digit(s[n-1]));
        for (int i = n-2; i >= 0; i--) {
            unsigned short x1 = char2digit(s[i]), x2 = char2digit(s[i+1]);
            int pair = pairDecodings(x1, x2);
            if (pair == -1) { // impossible pair, whole string can't be decoded
                return 0;
            }
            int single = singleDecodings(x1);
            decodeFrom[i] = pair*decodeFrom[i+2] + single*decodeFrom[i+1];
        }
        return decodeFrom[0];
    }
};
