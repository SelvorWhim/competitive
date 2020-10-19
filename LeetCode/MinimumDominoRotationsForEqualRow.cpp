/*
 * idea: for an equal row to be possible, one of the values in each domino
 * (and in particular, the first) must be present in every domino.
 * Then, just count which row is missing fewer of them.
 */

class Solution {
public:
    int minDominoRotationsX(vector<int>& A, vector<int>& B, int x) {
        const int n = A.size(); // == B.size()
        int countA = 0, countB = 0;
        for (int i = 0; i < n; i++) {
            if (A[i] == x) {
                countA++;
            }
            if (B[i] == x) {
                countB++;
            }
            if (A[i] != x && B[i] != x) {
                return -1;
            }
        }
        return min(n - countA, n - countB);
    }
    
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        int minRotationsA = minDominoRotationsX(A, B, A[0]);
        int minRotationsB = minDominoRotationsX(A, B, B[0]);
        if (minRotationsA < 0) {
            return minRotationsB;
        }
        else if (minRotationsB < 0) {
            return minRotationsA;
        }
        else {
            return min(minRotationsA, minRotationsB);
        }
    }
};
