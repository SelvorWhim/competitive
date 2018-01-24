class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return true;
        int n = matrix[0].size();
        // check all diagonals starting from the left column:
        for (int i = 0; i < m; i++) {
            int el = matrix[i][0]; // the element to repeat
            for (int j = 1; j < (m - i) && j < n; j++) {
                if (matrix[i+j][j] != el) {
                    return false;
                }
            }
        }
        // check remaining diagonals (from top row):
        for (int j = 1; j < n; j++) { // 1 because main diagonal was already checked
            int el = matrix[0][j]; // the element to repeat
            for (int i = 1; i < (n - j) && i < m; i++) {
                if (matrix[i][i+j] != el) {
                    return false;
                }
            }
        }
        return true; // all good
    }
};
