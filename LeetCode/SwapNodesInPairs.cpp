// based on examples, list length is not necessarily even. In that case I assume all but the last list member should be swapped in pairs.

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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL) return NULL;
        if (head->next == NULL) return head;
        ListNode* newHead = head->next;
        head->next = newHead->next;
        newHead->next = head;
        ListNode* ptr = head;
        while (ptr->next != NULL && ptr->next->next != NULL) {
            ListNode* n1 = ptr->next;
            ListNode* n2 = ptr->next->next;
            n1->next = n2->next;
            n2->next = n1;
            ptr->next = n2;
            ptr = n1;
        }
        return newHead;
    }
};
