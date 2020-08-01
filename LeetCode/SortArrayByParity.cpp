class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int n = A.size();
        int L = 0;
        int R = n-1;
        while (L < R) {
            // find first odd on left
            while (L < n && A[L] % 2 == 0) {
                L++;
            }
            
            // find last even on right
            while (R >= 0 && A[R] % 2 == 1) {
                R--;
            }
            
            // swap, unless they passed the intersection
            if (L < R) {
                int temp = A[L];
                A[L] = A[R];
                A[R] = temp;
            }
        }
        return A;
    }
};
