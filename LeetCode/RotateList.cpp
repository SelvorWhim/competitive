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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL) return NULL;
        ListNode* ptr = head;
        
        // measure list and connect the current ends:
        int len = 1;
        while (ptr->next != NULL) { // stops at last non-NULL node
            ptr = ptr->next;
            len++;
        }
        ptr->next = head; // list is now looped
        
        // break the new ends:
        ptr = head;
        for (int i = 0; i < len - (k % len) - 1; i++) {
            ptr = ptr->next;
        }
        head = ptr->next;
        ptr->next = NULL;
        return head;
    }
};
