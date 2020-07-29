class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int max_right = -1;
        for (int i = arr.size()-1; i>=0; i--) {
            int curr = arr[i];
            arr[i] = max_right;
            max_right = max(max_right, curr);
        }
        return arr;
    }
};
