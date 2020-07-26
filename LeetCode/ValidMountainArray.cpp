class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        if (A.size() < 3) {
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
            if (climbing && A[i-1] > A[i]) {
                // but the peak can't be at the left edge
                if (i == 1) {
                    return false;
                }
                climbing = false;
            }
        }
        return !climbing;
    }
};
