// based on examples, list length is not necessarily even, and if it's odd, all but the last list member should be swapped in pairs.

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
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0, head); // dummy node to enable switching pairs
        ListNode* it = &dummy;
        while (it->next != nullptr && it->next->next != nullptr) { // it is definitely not nullptr
            ListNode* after_pair = it->next->next->next;
            it->next->next->next = it->next;
            it->next = it->next->next;
            it->next->next->next = after_pair;
            it = it->next->next;
        }
        return dummy.next;
    }
};
