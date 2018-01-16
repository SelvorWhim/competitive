// idea: if we start at the edges and move (indexes) toward each other, knowing which one to move according to current sum, they should converge on the sum, assuming a unique solution exists
class Solution {
public:
	// simple O(N) implementation
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i_lo = 0, i_hi = numbers.size()-1;
        while (i_lo < i_hi) {
            int sum_curr = numbers[i_lo] + numbers[i_hi];
            if (sum_curr == target) {
                vector<int> ret = {i_lo+1, i_hi+1}; // 1-indexed indexes expected
                return ret;
            } else if (sum_curr > target) {
                i_hi--; // because sorted, this will reduce the sum
            } else { // (sum_curr < target)
                i_lo++; // because sorted, this will increase the sum
            }
        }
        return vector<int>(); // shouldn't get here if solution is guaranteed
    }
};
