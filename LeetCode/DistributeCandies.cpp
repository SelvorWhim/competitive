// idea: in an array of size 2n with k candy types, in a n+n split there will be at most k types if k<=n, and n otherwise. So min(k,n)

class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_set<int> cTypesSeen;
        for (auto &cType : candies) {
            cTypesSeen.insert(cType);
        }
        return min(cTypesSeen.size(), candies.size()/2);
    }
};
