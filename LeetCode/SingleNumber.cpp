class Solution {
public:
    // if there are two of each, we can insert each when we see it the first time and remove it when we see it again. The only number that will remain is the one that appears exactly once, because it's never removed. This way, in some cases less space is used (worst and average case is probably still O(n))
    int singleNumber(vector<int>& nums) {
        unordered_set<int> seen = unordered_set<int>();
        for (int i = 0; i < nums.size(); i++) {
            int curr = nums[i];
            unordered_set<int>::iterator curr_in_set = seen.find(curr);
            if (curr_in_set == seen.end()) {
                seen.insert(curr);
            } else {
                seen.erase(curr_in_set);
            }
        }
        return *seen.begin();
    }
	// as I later learned, there is a solution I hadn't considered that uses constant extra space (using XOR), but there's no solution faster than O(n), and this one's at least slightly better than O(n) space in most cases.
};
