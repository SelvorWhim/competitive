class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int next_expected = 1;
        for (int x: arr) {
            if (x == next_expected) {
                next_expected++;
            }
            else if (k > x - next_expected) {
                k -= x - next_expected;
                next_expected = x + 1;
            }
            else {
                return next_expected + k - 1;
            }
        }
        return next_expected + k - 1;
    }
};
