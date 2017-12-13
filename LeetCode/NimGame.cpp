class Solution {
public:
    // when it's your turn. More generally, if you can take anywhere from 1 to k stones on each turn, you can win if the number of stones is not divisible by k+1.
    bool canWinNim(int n) {
        return ((n % 4) != 0);
    }
};
