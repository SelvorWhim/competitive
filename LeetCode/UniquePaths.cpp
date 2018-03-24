// idea: the robot must take a total of m+n-2 steps, m-1 of them down and n-1 of them to the right. Any unique ordering of down steps and right steps is a unique path, and no other is possible under these limitations. Combinatorically, that's (m+n-2)!/((m-1)!*(n-1)!)
// problem: if we calculate the bigger factorial first and then divide, representation could be huge (up to 200!, under limitations, which is e375, too large for the guaranteed size of a long double). But if we start with (m+n-2)!/(n-1)! (assuming n>m), it should fit in a long double (e217 < e300)

class Solution {
public:
    int uniquePaths(int m, int n) {
        long double ret = 1.0;
        // assuming wlog m < n, find (m+n-2)!/(n-1)! directly, without calculating the bigger number (multiply all numbers from n to m+n-2)
        for (int i = max(m,n); i <= m+n-2; i++) {
            ret *= i;
        }
        // now (under same assumption wlog) divide by (m-1)!
        for (int i = min(m,n)-1; i > 1; i--) {
            ret /= i;
        }
        return ret;
    }
};
