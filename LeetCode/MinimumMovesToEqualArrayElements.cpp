// equivalently (as far as differences between elements are concerned), decrement one element by 1 every move. That makes the problem simpler - you decrement the biggest number until it reaches the second biggest, then both (or more, if there are equal elements) until they reach the third biggest value, etc, with the smallest being the only one that doesn't eed reducing. This could be calculated by sorting, or counting the elements and then sorting
// or, a different equivalent...deduct the smallest value from everything, then sum everything! Pretty sure that would work even with negative numbers. This one's linear!

class Solution {
public:
    int minMoves(vector<int>& nums) {
        int min = *std::min_element(nums.begin(),nums.end());
        int fullSum = std::accumulate(nums.begin(), nums.end(), 0); // sums by default
        return fullSum - (min * nums.size()); // sum after deducing the minimum from each / deducing the minimum n times
    }
};
