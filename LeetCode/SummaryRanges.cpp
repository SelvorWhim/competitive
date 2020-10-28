class Solution {
public:
    string range_to_string(int range_min, int range_max) {
        if (range_min == range_max) {
            return std::to_string(range_min);
        }
        std::ostringstream oss;
        oss << range_min << "->" << range_max;
        return oss.str();
    }
    
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ret;
        if (nums.size() == 0) {
            return ret;
        }
        int curr_range_min = nums[0];
        int curr_range_max = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == curr_range_max + 1) {
                curr_range_max++;
            }
            else {
                ret.push_back(range_to_string(curr_range_min, curr_range_max));
                curr_range_min = nums[i];
                curr_range_max = nums[i];
            }
        }
        ret.push_back(range_to_string(curr_range_min, curr_range_max));
        return ret;
    }
};
