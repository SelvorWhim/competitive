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
	// implementation with 2 iterators, one going in double steps. If there is a cycle, this guarantees they will meet regardless of where the cycle starts, while using O(1) extra space. (Not my idea, got it while searching for an answer to an interview question online, but my implementation.)
    bool hasCycle(ListNode *head) {
        ListNode* it1 = head;
        ListNode* it2 = head;
        while (it2 != NULL) {
            it1 = it1->next;
            it2 = it2->next;
            if (it1 == NULL || it2 == NULL) return false;
            it2 = it2->next;
            if (it1 == it2) return true;
        }
        return false;
    }
};
