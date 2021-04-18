// under givens, we shouldn't end up running into nullptrs, so some edge case handling is omitted
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // make front_p n steps in front of back_p
        ListNode* back_p = head;
        ListNode* front_p = head;
        for (int i = 0; i < n; i++) {
            front_p = front_p->next;
        }
        if (front_p == nullptr) {
            return head->next;
        }
        while (front_p->next != nullptr) {
            back_p = back_p->next;
            front_p = front_p->next;
        }
        back_p->next = back_p->next->next;
        return head;
    }
};
