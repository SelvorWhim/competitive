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
    ListNode* middleNode(ListNode* head) {
        ListNode* it = head;
        int len = 0;
        while (it != NULL) {
            it = it->next;
            len++;
        }
        it = head;
        for (int i = 0; i < len/2; i++) {
            it = it->next;
        }
        return it;
    }
};
