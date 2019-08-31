class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // group the strings by their sorted version (which will be the same for anagrams) using multimap
        multimap<string, string> map_groups;
        for (string s : strs) {
            string sorted_s(s); // not actually sorted yet :P
            sort(sorted_s.begin(), sorted_s.end()); // now it is
            map_groups.insert(pair<string,string>(sorted_s, s));
        }
        
        // convert each multimap group to vector<string>, return vector of vectors
        vector<vector<string>> groups;
        multimap<string, string>::iterator group_it;
        for(auto it = map_groups.begin(); it != map_groups.end(); it = group_it) {
            vector<string> group;
            auto map_group = map_groups.equal_range((*it).first);
            for (group_it = map_group.first;  group_it != map_group.second;  ++group_it)
            {
                group.push_back((*group_it).second);
            }
            groups.push_back(group);
        }
        return groups;
    }
};
