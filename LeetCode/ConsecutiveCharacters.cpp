class Solution {
public:
    int maxPower(string s) {
        int curr_len = 0;
        int max_len = 0;
        char curr_char = s[0]; // given s's length is at least 1
        for (char c : s) {
            if (c == curr_char) {
                curr_len++;
            }
            else {
                max_len = max(max_len, curr_len);
                curr_char = c;
                curr_len = 1;
            }
        }
        max_len = max(max_len, curr_len);
        return max_len;
    }
};
