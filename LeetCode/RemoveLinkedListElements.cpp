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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* it = head;
        ListNode* newHead = NULL;
        ListNode* lastValid = NULL;
        while (it != NULL) {
            if (it->val != val) {
                if (newHead == NULL) {
                    newHead = it;
                }
                if (lastValid == NULL) {
                    lastValid = it;
                } else {
                    lastValid = lastValid->next;
                }
            }
            else if (it->val == val && lastValid != NULL) {
                lastValid->next = it->next;
            } // if (it->val == val && lastValid == NULL), the node is effectively skipped in the new list
            it = it->next;
        }
        return newHead;
    }
};
