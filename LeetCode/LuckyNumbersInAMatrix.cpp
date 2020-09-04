// O(n*m) solution for n*m matrix dimensions
// can't find all potential lucky numbers without checking all matrix elements at least once, so can't do much better

class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> ret;
        if (matrix.size() == 0) {
            return ret;
        }
        
        vector<int> row_mins;
        for (int i = 0; i < matrix.size(); i++) {
            row_mins.push_back(matrix[i][0]);
            for (int j = 1; j < matrix[0].size(); j++) {
                row_mins.back() = min(row_mins.back(), matrix[i][j]);
            }
        }
        
        vector<int> col_maxs;
        for (int j = 0; j < matrix[0].size(); j++) {
            col_maxs.push_back(matrix[0][j]);
            for (int i = 1; i < matrix.size(); i++) {
                col_maxs.back() = max(col_maxs.back(), matrix[i][j]);
            }
        }
        
        for (int m : row_mins) {
            for (int n : col_maxs) {
                if (m == n) {
                    ret.push_back(m);
                }
            }
        }
        
        return ret;
    }
};
