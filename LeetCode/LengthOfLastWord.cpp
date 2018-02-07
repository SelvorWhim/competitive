class Solution {
public:
    int lengthOfLastWord(string s) {
        bool startedWord = false;
        int lastWordLen = 0;
        for (int i = s.length()-1; i >= 0; i--) { // iterate backwards
            if (startedWord && s[i] == ' ') break; // passed the last word
            if (s[i] != ' ') {
                startedWord = true;
                lastWordLen++;
            }
        }
        return lastWordLen;
    }
};
