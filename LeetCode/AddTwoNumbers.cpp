// since the lists are stored from least significant digits (which are both units) and the expected output likewise, we can use the normal manual addition algorithm

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *lSum = new ListNode(0); // dummy node for convenience
        ListNode *it1 = l1, *it2 = l2, *itSum = lSum;
        int carry = 0;
        while (it1 != NULL || it2 != NULL) {
            int sum = (it1 == NULL ? 0 : it1->val)
					+ (it2 == NULL ? 0 : it2->val)
					+ carry;
            carry = sum / 10;
            sum = sum % 10;
            itSum->next = new ListNode(sum);
            if (it1 != NULL) {
                it1 = it1->next;
            }
            if (it2 != NULL) {
                it2 = it2->next;
            }
            itSum = itSum->next;
        }
        if (carry > 0) {
            itSum->next = new ListNode(carry);
        }
        return lSum->next; // skip dummy node
    }
};
