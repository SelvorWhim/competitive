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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* ptr = head; // iterates over all nodes
        ListNode* firstWithVal = head; // iterates over nodes which are first in sublist of duplicates
        while (ptr != NULL) {
            while (ptr != NULL && ptr->val == firstWithVal->val) {
                ptr = ptr->next;
            }
            firstWithVal->next = ptr; // first of the last sublist of duplicates will get NULL, as it should
            firstWithVal = firstWithVal->next;
        }
        return head;
    }
};
