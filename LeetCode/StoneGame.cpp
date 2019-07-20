/*
// at each point you choose first or last in the line
// I'd guess optimal play aims to maximize score, where your score is your total stones minus opponent's total
// all I need is to know whether the score at the end is positive (I win) or negative (I lose), no optimal path reconstruction necessary (makes sense, since there's 2 agents here, I'd have to react to opponent's moves anyway)
// to know the score of the optimal move, for which there are 2 choices, I need to know the opponent's optimal move score following each choice. Each next move is for a shorter row. Can build from shortest row.
// possible board states can be represented by every possible ordered pair of indexes, so need a 2d table for dynamic solution
*/

class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();
        
        // initialize subproblem solution storage - triangular matrix starting with longer rows
        vector<vector<int>> opt_move(n);
        for (int i = 0; i < n; i++) {
            opt_move[i] = vector<int>(n-i);
            opt_move[i][0] = piles[i]; // optimal move with just 1 pile left is to take the pile
        }
        
        // solve subproblems: opt_move[i][k] = your best score for a row starting at index i and ending at i+k
        for (int k = 1; k < n; k++) { // solution for subproblem with a row of length k+1 (index difference k); k=0 already initialized
            for (int i = 0; i < n-k; i++) { // solution for subproblem starting at i
                opt_move[i][k] = max(piles[i] - opt_move[i+1][k-1], piles[i+k] - opt_move[i][k-1]);
            }
        }
        
        return opt_move[0][n-1] > 0;
    }
};
