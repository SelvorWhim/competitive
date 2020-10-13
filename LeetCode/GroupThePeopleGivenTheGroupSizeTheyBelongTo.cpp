// idea: people in the same group have the same number of people in their group (the reverse is not necessarily true)

class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> ret;
        map<int,vector<int>> size_to_ids;
        for (int i = 0; i < groupSizes.size(); i++) {
            size_to_ids[groupSizes[i]].push_back(i); // creates new vector first if size_to_ids doesn't have the group size yet
        }
        
        for (auto const& groupable : size_to_ids)
        {
            // groupable.first is group size, groupable.second is a vector of all indexes in a group that size
            for (int i = 0; i < groupable.second.size(); i++) {
                // ids.size() / groupSize subvectors
                if (i % groupable.first == 0) {
                    ret.push_back(vector<int>());
                }
                ret.back().push_back(groupable.second[i]);
            }
        }
        
        return ret;
    }
};
