class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        make_heap(stones.begin(), stones.end()); // max heap
        while (stones.size() > 1) {
            int heaviest_stone = stones.front();
            pop_heap(stones.begin(), stones.end());
            stones.pop_back();
            int second_heaviest_stone = stones.front();
            pop_heap(stones.begin(), stones.end());
            stones.pop_back();
            if (heaviest_stone > second_heaviest_stone) {
                stones.push_back(heaviest_stone - second_heaviest_stone);
                push_heap(stones.begin(), stones.end());
            }
        }
        if (stones.size() == 0) {
            return 0;
        }
        return stones.front();
    }
};
