class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int specials_count = 0;
        int m = mat.size();
        int n = mat[0].size();
        for (int row_i = 0; row_i < m; row_i++) {
            // iterate over rows
            int special_col_i = -1;
            for (int col_i = 0; col_i < n; col_i++) {
                // iterate over columns looking for a number that looks special in its row
                if (mat[row_i][col_i] != 0) {
                    if (special_col_i >= 0) {
                        // 2nd non-zero in same column, so it can't be special
                        special_col_i = -1;
                        break;
                    }
                    else {
                        special_col_i = col_i;
                    }
                }
            }
            if (special_col_i < 0) {
                // row is full of zeroes, so it has no special
                continue;
            }
            for (int row_j = 0; row_j < m; row_j++) {
                // potential special was found, now check if the rest of its column is zeroes
                if (row_j == row_i) {
                    continue;
                }
                if (mat[row_j][special_col_i] != 0) {
                    special_col_i = -1;
                    break;
                }
            }
            if (special_col_i >= 0) {
                specials_count++;
            }

        }
        return specials_count;
    }
};
