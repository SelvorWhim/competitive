// each array member has to be added to the sum according to the number of odd-length subarrays it appears in
// each appears in 1 1-length, and 3 3-length unless it's near the edge, and 5 5-length with the same exception etc.
// until the biggest odd that fits in the array length
// if you're kth from the nearest edge, you appear in min(n, k) n-length subarrays
// O(n^2) solution - there may be a closed formula for the inner loop but given n<=100, n^2 should be fine

class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int sum = 0;
        int n = arr.size();
        int n_odd = (n%2==0) ? n-1 : n;
        for (int i = 0; i < n; i++) {
            int k = std::min(i+1, n-i);
            for (int j = 1; j <= n_odd; j += 2) {
                int times = std::min(std::min(j, k), n-j+1);
                sum += times * arr[i];
                //cout << arr[i] << " appears " << times << " times in " << j << "-length subarrays" << endl;
            }
        }
        return sum;
    }
};
