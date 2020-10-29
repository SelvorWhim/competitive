// hah, nice natural setup
// look at the gaps and look for the max distance per gap
// when there's a gap at the end of a row, the max distance there is the length of the gap
// when there's a gap between people, the max distance there is the length of the gap divided by 2 (rounded up)

class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        bool is_left_edge_gap = true;
        int curr_gap_len = 0;
        int max_dist = 0;
        for (int i = 0; i < seats.size(); i++) {
            if (seats[i] == 0) {
                curr_gap_len++;
            }
            else {
                if (is_left_edge_gap) {
                    max_dist = curr_gap_len;
                    is_left_edge_gap = false;
                }
                else {
                    int curr_dist = ceil(curr_gap_len/2.0);
                    max_dist = max(max_dist, curr_dist);
                }
                curr_gap_len = 0;
            }
        }
        if (seats.back() == 0) {
            // right edge gap
            max_dist = max(max_dist, curr_gap_len);
        }
        return max_dist;
    }
};
