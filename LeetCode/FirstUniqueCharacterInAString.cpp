template<class T> // generic for future use...
bool contains(const unordered_set<T>& container, const T& element) {
    return container.find(element) != container.end();
}

class Solution {
public:
    int firstUniqChar(string s) {
        unordered_set<char> once, multiple; // seen
        for(char& c : s) {
            if (contains(once,c)) {
                once.erase(c);
                multiple.insert(c);
            } else if (!contains(multiple,c)) {
                once.insert(c);
            }
        }
        for (int i = 0; i < s.length(); i++) {
            if (contains(once,s[i])) {
                return i;
            }
        }
        return -1;
    }
};
