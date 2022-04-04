/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* follow = head;
        ListNode* lead = head; // will be set to k in front of the back one
        for (int i = 0; i < k-1; i++) {
            lead = lead->next;
        }
        ListNode* swapped1 = lead; // kth node
        while (lead->next != nullptr) {
            lead = lead->next;
            follow = follow->next;
        }
        // follow is now kth from end
        int val_temp = follow->val;
        follow->val = swapped1->val;
        swapped1->val = val_temp;
        return head;
    }
};