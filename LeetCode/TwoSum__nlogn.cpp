/* this version sorts, then proceeds like InputIsSorted version of the problem
 * for O(n*log(n)) performance
 */
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        int i = 0, j = n-1;
        vector<pair<int, int> > indexed_nums(n); // keep track of original indexes 
        for (int i = 0; i < n; ++i) { 
            indexed_nums[i] = (make_pair(nums[i], i)); 
        } 

        // Sorting pair vector 
        sort(indexed_nums.begin(), indexed_nums.end()); // sorts by 1st element first, which is the original value
        while (i < j) {
            int currSum = indexed_nums[i].first + indexed_nums[j].first;
            if (currSum == target) {
                return vector<int> {indexed_nums[i].second,indexed_nums[j].second};
            }
            else if (currSum < target) {
                i++;
            }
            else { // currSum > target
                j--;
            }
        }
        return vector<int>(); // shouldn't happen
    }
};
