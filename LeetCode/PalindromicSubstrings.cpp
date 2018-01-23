// idea: expand around palindrome centers. O(number of palindromes), which is O(N^2) if there's long sequences of identical characters, otherwise more like O(N)

class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        int n = s.size();
        // count odd-lengthed palindromes
        for (int i = 0; i < n; i++) {
            for (int j = 0; i-j >= 0 && i+j < n; j++ ) { // expanding outwards from palindrome center
                if (s[i-j] == s[i+j]) {
                    count++;
                } else {
                    break;
                }
            }
        }
        // count even-lengthed palindromes
        for (int i = 1; i < n; i++) {
            for (int j = 0; i-j >= 1 && i+j < n; j++ ) { // expanding outwards from palindrome center
                if (s[i-j-1] == s[i+j]) {
                    count++;
                } else {
                    break;
                }
            }
        }
        return count;
    }
};
