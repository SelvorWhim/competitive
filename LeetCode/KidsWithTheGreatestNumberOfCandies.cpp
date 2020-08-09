class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> ret;
        int n = candies.size();
        if (n == 0) {
            return ret;
        }
        
        // find max
        int max = candies[0];
        for (int i = 1; i < n; i++) {
            if (candies[i] > max) {
                max = candies[i];
            }
        }
        
        // for each kid, the answer depends on if giving them all the candies will make them >=max
        for (int i = 0; i < n; i++) {
            ret.push_back(candies[i] + extraCandies >= max);
        }
        
        return ret;
    }
};
