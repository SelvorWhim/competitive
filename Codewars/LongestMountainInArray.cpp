class Solution {
public:
    int longestMountain(vector<int>& A) {
        int max_mt_len = 0;
        int curr_mt_len = 1;
        bool going_up = false;
        bool going_down = false;
        for (int i = 1; i < A.size(); i++) {
            if (A[i-1] < A[i]) {
                going_down = false;
                if (going_up) { // up slope on current mountain
                    curr_mt_len++;
                }
                else { // up slope on new mountain
                    max_mt_len = max(curr_mt_len, max_mt_len);
                    curr_mt_len = 2;
                    going_up = true;
                }
            }
            else if (A[i-1] > A[i]) {
                if (going_up) { // just past the peak
                    curr_mt_len++;
                    going_up = false;
                    going_down = true;
                }
                else if (going_down) { // continuing down slope
                    curr_mt_len++;
                }
            }
            else {
                going_up = false;
                going_down = false;
            }
        }
        if (going_down) {
            max_mt_len = max(curr_mt_len, max_mt_len);
        }
        if (max_mt_len < 3) {
            max_mt_len = 0;
        }
        return max_mt_len;
    }
};
