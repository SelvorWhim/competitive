// both numbers are >=1 so just find the 2 biggest numbers at different indexes
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max1 = 0, max2 = 0; // given nums are all positive; keep max1 >= max2
        for (int n : nums) {
            if (n >= max1) {
                max2 = max1;
                max1 = n;
            }
            else if (n > max2) {
                max2 = n;
            }
        }
        return (max1 - 1) * (max2 - 1); // I know it says product but them's the requirements
    }
};
