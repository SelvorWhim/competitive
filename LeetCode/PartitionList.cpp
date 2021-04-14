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
    ListNode* partition(ListNode* head, int x) {
        // set smallHead to be the first value <x - the head of the new list
        ListNode* smallHead = head;
        while (smallHead != nullptr && smallHead->val >= x) {
            smallHead = smallHead->next;
        }
        if (smallHead == nullptr) {
            return head;
        }

        // set smallHead to be the first value >=x - the head of the right partition
        ListNode* bigHead = head;
        while (bigHead != nullptr && bigHead->val < x) {
            bigHead = bigHead->next;
        }
        if (bigHead == nullptr) {
            return head;
        }

        // build both partitions
        ListNode* lastSmall = smallHead;
        ListNode* lastBig = bigHead;
        while (head != nullptr) {
            ListNode* temp = head->next; // otherwise head iterator gets stuck in a loop
            if (head->val < x) {
                lastSmall->next = head;
                lastSmall = lastSmall->next;
            }
            else {
                lastBig->next = head;
                lastBig = lastBig->next;
            }
            head = temp;
        }

        // bring them together
        lastSmall->next = bigHead;
        lastBig->next = nullptr;
        return smallHead;
    }
};
