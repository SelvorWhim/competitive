class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int n = startTime.size(); // assumed to be <= endTime.size()
        int busyAtQueryTime = 0;
        for (int i = 0; i < n; i++) {
            if (startTime[i] <= queryTime && endTime[i] >= queryTime) {
                busyAtQueryTime++;
            }
        }
        return busyAtQueryTime;
    }
};
