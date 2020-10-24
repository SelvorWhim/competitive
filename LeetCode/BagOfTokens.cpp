// play order doesn't matter - global optimization
// each token represents a trade between its value in power and 1 score
// so the optimal strategy probably involves trading power for score on the lowest value tokens
// and trading score for power on the highest value tokens
// (but a few in the middle may end up useless, in which case don't play them - tracking max_score solves this)

class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int P) {
        sort(tokens.begin(), tokens.end());
        int power = P;
        int score = 0;
        int max_score = 0;
        int i_low = 0, i_high = tokens.size() - 1;
        while (i_low <= i_high) {
            if (power >= tokens[i_low]) {
                power -= tokens[i_low];
                score++;
                max_score = max(max_score, score);
                i_low++;
            }
            else if (score >= 1) {
                power += tokens[i_high];
                score--;
                i_high--;
            }
            else {
                break;
            }
        }
        return max_score;
    }
};
