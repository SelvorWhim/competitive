// there's built-in solutions, but I'mma do this proper like :P

class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0) return "0";
        bool positive = num >= 0;
        num = abs(num);
        string s = "";
        while (num > 0) {
            s = to_string(num%7) + s; // maybe it copies the string each time, but based on value range it's only ever <=10 characters long
            num = num / 7;
        }
        if (positive) {
            return s;
        } else {
            return "-" + s;
        }
    }
};
