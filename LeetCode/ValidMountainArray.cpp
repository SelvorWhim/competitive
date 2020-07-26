class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        if (A.size() < 3 || A[0] > A[1]) {
            return false;
        }
        bool climbing = true;
        // must check whole array for rule, any pair can break it
        for (int i = 1; i < A.size(); i++) {
            // flat breaks the rule
            if (A[i] == A[i-1]) {
                return false;
            }
            // climbing after starting descent breaks the rule
            if (!climbing && A[i-1] < A[i]) {
                return false;
            }
            // in this case i-1 is the point where we reach the peak (if this is a valid mountain)
            // (2nd edge case check makes sure the "peak" isn't i==0)
            if (climbing && A[i-1] > A[i]) {
                climbing = false;
            }
        }
        return !climbing;
    }
};
