// idea: search from front and back for next vowel, switch. Stop when indexes converge or pass each other.

class Solution {
private:
    bool isVowel(char c) {
        char lc = tolower(c);
        return lc=='a' || lc=='e' || lc=='i' || lc=='o' || lc=='u';
    }
public:
    string reverseVowels(string s) {
        int n = s.length();
        int i1 = 0, i2 = n-1;
        while (i1 < i2 && i1 < n-1 && i2 > 0) {
            while (i1 < n-1 && !isVowel(s[i1])) i1++; // find next vowel
            if (i1 >= i2) break;
            while (i2 > 0 && !isVowel(s[i2])) i2--; // find previous vowel
            // switch:
            char temp = s[i1];
            s[i1] = s[i2];
            s[i2] = temp;
            // don't get stuck:
            i1++;
            i2--;
        }
        return s;
    }
};
