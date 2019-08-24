// assuming intervals are presented with beginning first, then end (interval[0] < interval[1])
class Solution {
public:
    // I would've made it a list of pairs but this is the given setup
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> merged;
        if (intervals.empty()) return merged;
        sort(intervals.begin(), intervals.end()); // sorts by 1st member (interval start) then by 2nd (interval end)
        merged.push_back(intervals[0]);
        for (auto interval : intervals) {
            if (interval[0] <= merged.back()[1]) { // due to sorting, this guarantees intersection with last merged
                merged.back()[1] = max(merged.back()[1], interval[1]); // max in case 2nd is contained interval
            }
            else { // new independent interval
                merged.push_back(interval);
            }
        }
        return merged;
    }
};
