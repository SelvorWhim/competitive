// TODO: fix failing case: [1,0,1,0,0]
// TODO: optimize: iterate back only till 1st 0

class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        int shift = 0;
        for (int i = 0; (i + shift) < n; i++) {
            if (arr[i] == 0) {
                shift++;
            }
        }
        cout << shift << endl;
        cout << (n - shift) - 1;
        for (int i = n - shift - 1; i >= 0; i--) {
            if (i+shift < n) {
                arr[i+shift] = arr[i];
            }
            if (arr[i] == 0) {
                shift--;
                arr[i+shift] = arr[i];
            }
        }
    }
};
