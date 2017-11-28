class Solution {
public:
	// need to output all rows of Pascal's triangle up to a point, so there's nothing to gain by discarding previous rows to save space or using the closed formula, every member needs to be set anyway, and each is O(1) to calculate this way.
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> rows = vector<vector<int>>(numRows);
        for (int i = 0; i < numRows; i++) {
            rows[i] = vector<int>(i+1);
            rows[i][0] = 1;
            rows[i][i] = 1;
            for (int j = 1; j < i; j++) { // for the first two rows, the loop will close immediately, for the rest the indexes work
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j];
            }
        }
        return rows;
    }
};
