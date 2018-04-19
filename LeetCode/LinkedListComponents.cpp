/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int numComponents(ListNode* head, vector<int>& G) {
        set<int> setG(G.begin(), G.end());
        bool inConnected = false;
        int connectedCount = 0;
        ListNode* ptr = head;
        while (ptr != NULL) {
            if (setG.find(ptr->val) != setG.end()) { // if this member is in G
                if (!inConnected) {
                    connectedCount++;
                }
                inConnected = true;
            } else if (inConnected) {
                    inConnected = false;
            }
            ptr = ptr->next;
        }
        return connectedCount;
    }
};
