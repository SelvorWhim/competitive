class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        int i_plus = a.find('+',0);
        int ar = stoi(a.substr(0, i_plus), nullptr);
        int ai = stoi(a.substr(i_plus+1), nullptr); // stoi should stop at the i, not throw an error
        i_plus = b.find('+',0);
        int br = stoi(b.substr(0, i_plus), nullptr);
        int bi = stoi(b.substr(i_plus+1), nullptr);
        int cr = (ar * br) - (ai * bi);
        int ci = (ar * bi) + (ai * br);
        return to_string(cr) + "+" + to_string(ci) + "i";
    }
};
