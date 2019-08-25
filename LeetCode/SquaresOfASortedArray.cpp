class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        if (A.empty()) return vector<int>(0);
        int n = A.size();
        if (A[0] > 0) {
            // in-place, mutating
            std::for_each(A.begin(), A.end(), [](int &n){ n=n*n; });
            return A;
        }
        if (A[n-1] < 0) {
            std::reverse(A.begin(),A.end());
            std::for_each(A.begin(), A.end(), [](int &n){ n=n*n; });
            return A;
        }
        vector<int> sA(n);
        int firstPositive = 0;
        while (firstPositive < n && A[firstPositive] <= 0) firstPositive++; // optimization: binary search to find 0 more efficiently
        int lastNegative = firstPositive - 1;
        for (int i = 0; i < n; i++) {
            if (firstPositive < n && (lastNegative < 0 || A[firstPositive] < -A[lastNegative])) {
                sA[i] = A[firstPositive]*A[firstPositive];
                firstPositive++;
            }
            else {
                sA[i] = A[lastNegative]*A[lastNegative];
                lastNegative--;
            }
        }
        return sA;
    }
};
