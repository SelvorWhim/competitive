// idea: s is a subsequence iff within t we find its first character, then its second, etc. till the last, with arbitrary other characters in between. We can just keep looking for the next relevant letter until we find them all or reach the end of t.

class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.size() == 0) return true;
        if (s.size() > t.size()) return false;
        int i = 0; // index within s we're trying to find in t
        for (int j = 0; j < t.size(); j++) { // index within t
            if (s[i] == t[j]) {
                i++;
                if (i >= s.size()) return true;
            }
        }
        return false;
    }
};
