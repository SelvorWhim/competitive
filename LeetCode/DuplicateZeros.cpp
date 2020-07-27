// suboptimal solution, starting with it to help debug a solution that doesn't use extra space
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        int arr2[2*n];
        for (int i=0, i2=0; i<n; i++, i2++) {
            arr2[i2] = arr[i];
            if (arr[i]==0) {
                i2++;
                arr2[i2] = arr[i];
            }
        }
        for (int i=0; i<n; i++) {
            arr[i] = arr2[i];
        }
    }
};
