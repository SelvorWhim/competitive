class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int x : nums) {
            if (seen.find(x) == seen.end()) {
                seen.insert(x);
            }
            else {
                return true;
            }
        }
        return false;
    }
};
