/* idea: start with the fast/slow iterators.
 * slow will move a to loop start, then b more to meeting point,
 * while fast will take an extra loop to get there:
 * 2*(a+b)=a+b+loop_len -> a+b=loop_len
 * move a steps forward from meeting to get to start of loop,
 * while another moves a from head to get there. You don't know what a is
 * but that is where they'll meet!
 */

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
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return NULL;
        }
        ListNode *slow = head;
        ListNode *fast = head;
        do {
            slow = slow->next;
            fast = fast->next->next;
        } while (slow != fast && fast != NULL && fast->next != NULL);
        if (slow != fast) {
            return NULL;
        }
        fast = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }
};
