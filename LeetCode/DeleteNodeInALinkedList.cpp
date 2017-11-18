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
    // idea: since we cannot redirect the pointer of the previous node (if one exists), we must turn it into the next node and delete that one.
    // if this is the tail, we'd have to make an existing pointer to it point at NULL, which would be impossible, but that case is excluded
    void deleteNode(ListNode* node) {
        ListNode* temp = node->next; // node!=tail, so we know node->next exists
        node->val = temp->val;
        node->next = temp->next;
        delete temp; // will free previous next node, but not whatever it points to (rest of the list)
    }
};
