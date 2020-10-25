class Solution {
private:
    map<int, bool> dp; // true if you can win when given this number and both playing optimally, false if not
public:
    bool winnerSquareGame(int n) {
        // iterating downwards makes good use of memoization, unlike reverse loop which always starts by decrementing 1 so it ends up going over all the options (and isn't fast enough)
        for (int i = floor(sqrt(n)); i >= 1; i--) {
            int next_turn = n - (i*i);
            if(dp.find(next_turn) == dp.end()) {
                // no solution for this subproblem yet - memoize
                bool next_player_can_win = winnerSquareGame(next_turn);
                if (!next_player_can_win) {
                    return true;
                }
                dp[next_turn] = !next_player_can_win;
            }
            
        }
        return false;
    }
};
