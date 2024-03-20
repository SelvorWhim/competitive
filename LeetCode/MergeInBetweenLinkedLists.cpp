// Constraints remove edge cases like adding list 2 before or after all the elements of list1

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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* it = list1;
        for (int i = 0; i < a-1; i++) {
            it = it->next;
        }
        ListNode* it2 = it;
        it = it->next;
        it2->next = list2;
        for (int i = a; i < b+1; i++) {
            it = it->next;
        }
        while (it2->next != nullptr) {
            it2 = it2->next;
        }
        it2->next = it;
        return list1;
    }
};
