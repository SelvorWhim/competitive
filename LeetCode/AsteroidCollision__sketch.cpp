// collisions will be between positive asteroid followed by negative

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        bool right_found; // found first asteroid going right (positive sign)
        vector<int> ret;
        for (a : asteroids) {
            if (a < 0 && !right_found) {
                ret.push_back(a);
            }
            else if (a >)
        }
    }
};
