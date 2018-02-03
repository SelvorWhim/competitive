// this solution passed at least 108/123 cases, the shown failed case input was not fully displayed so I don't know what's wrong.

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        double lastKSum = 0, bestKSum = INT_MIN;
        int lastK[k] = {}; // CIRCULAR array, to avoid shifting by k every time. Initialized as 0.
        int lastKi = 0; // index within circular array - next element will be placed/replaced here
        // todo: initialize w 0
        for (int i = 0; i < n; i++) {
            lastKi = i % k;
            lastKSum -= lastK[lastKi];
            lastKSum += nums[i];
            lastK[lastKi] = nums[i];
            bestKSum = max(bestKSum, lastKSum);
        }
        return bestKSum / (min(k,n)); // based on failed example, input may have n < k, and in that case the max average is the total average
    }
};
