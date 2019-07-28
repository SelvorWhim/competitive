/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
// the obvious
class Solution1 {
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

// the less obvious (but actually slower)
class Solution2 {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* mid = head;
        ListNode* end = head;
        while (end != NULL) {
            end = end->next;
            if (end != NULL) {
                end = end->next;
                mid = mid->next;
            }
        }
        return mid;
    }
};