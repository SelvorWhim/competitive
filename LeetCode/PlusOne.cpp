class Solution {
public:
	// this solution mutates original vector
    vector<int> plusOne(vector<int>& digits) {
        for (int i=digits.size() - 1; i>=0; i--) {
            digits[i] = (digits[i]+1)%10;
            if (digits[i] > 0) break;
        }
        if (digits[0] == 0) { // assuming no leading zeroes unless original number was 0, this means we had overflow up to most significant digit
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
