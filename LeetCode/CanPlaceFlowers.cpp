// in any gap of n 0's, you can place up to ceil((n-2)/2) flowers
// can be slightly optimized by checking against n at intervals, but this is the simplest solution

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int gap_len = 1; // left edge gap is equivalent to a gap with 1 more 0 on the left
        int max_placeable = 0;
        for (int flower : flowerbed) {
            if (flower == 0) {
                gap_len++;
            }
            else if (gap_len > 0) { // gap just ended
                max_placeable += ceil((gap_len-2)/2.0);
                gap_len = 0;
            }
        }
        if (gap_len > 0) { // gap just ended
            max_placeable += ceil((gap_len-1)/2.0); // -1 in this case because it's a gap at the right edge, with no blocking flower after it
        }
        return max_placeable >= n;
    }
};
