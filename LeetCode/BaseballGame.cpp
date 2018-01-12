// based on the examples, when a round's score is calculated by "+" or "D", the last valid round(s) remain (in the end sum) (unless later canceled)
// could be multiple (unlimited) C's, so it's not enough to keep track of the last 1/2 valid rounds (+sum).
// idea: use a stack to keep track of all previous valid rounds. Number of rounds <= 1000, so this shouldn't take too much space.

class Solution {
public:
    // this implementation assumes all strings are in one of the valid formats, and certain things about how to handle edge cases with no examples
    int calPoints(vector<string>& ops) {
        int sum = 0;
        stack<int> valid;
        for(auto it = ops.begin(); it != ops.end(); it++) {
            if (*it == "C") {
                if (!valid.empty()) { // otherwise nothing is done, I guess?
                    sum -= valid.top();
                    valid.pop();
                }
            } else if (*it == "D") {
                if (!valid.empty()) { // no examples given for what to do otherwise, I'll assume it's like 0, doesn't affect the sum so nothing is pushed
                    int curr = 2*valid.top();
                    valid.push(curr);
                    sum += curr;
                }
            } else if (*it == "+") {
                if (valid.size() >= 2) { // expected case
                    int last = valid.top();
                    valid.pop();
                    int before_last = valid.top();
                    valid.push(last);
                    int curr = last + before_last;
                    valid.push(curr);
                    sum += curr;
                } else if (valid.size() == 1) { // stack had one last round...I guess we'll add the sum of that round and 0?
                    valid.push(valid.top());
                    sum += valid.top();
                }
                // else empty, by assumption do nothing 
            } else { // input assumed valid
                int curr = stoi(*it);
                valid.push(curr);
                sum += curr;
            }
        }
        return sum;
    }
};
