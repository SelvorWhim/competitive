class Solution {
private:
    // number of slices included in a slice of size n
    // f(3) = 1, f(4) = 3, f(5) = 6, f(6) = 10
    // sum of 1, sum of 2, sum of 3 integers etc... if n started from 1 it would be f(n) = n(n+1)/2
    // closed formula: f(n) = (n-2)(n-1)/2
    int numberOfSubslices(int n) {
        if (n < 3) return 0;
        return (n-2)*(n-1)/2;
    }
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int n = A.size();
        if (n < 3) return 0;
        int total = 0;
        int lastInterval = A[1] - A[0];
        int streak = 2; // number of array members, not intervals
        for (int i = 2; i < n; i++) {
            int interval = A[i] - A[i-1];
            if (interval == lastInterval) {
                streak++;
            } else {
                total += numberOfSubslices(streak);
                lastInterval = interval;
                streak = 2;
            }
        }
        total += numberOfSubslices(streak);
        return total;
    }
};
