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
    // simpler than my original idea, assuming no loops in the lists. O(m+n) time, O(1) extra space
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // first find the length of both lists: O(m+n)
        ListNode* itA = headA;
        ListNode* itB = headB;
        int lenA = 0, lenB = 0;
        while (itA != NULL) {
            itA = itA->next;
            lenA++;
        }
        while (itB != NULL) {
            itB = itB->next;
            lenB++;
        }
        
        // now make the iterators equal distances from the end, with the one for the shorter list at the list's head, so it's guaranteed to contain the intersection if one exists: O(|m-n|)
        itA = headA;
        itB = headB;
        while (lenA > lenB) {
            itA = itA->next;
            lenA--;
        }
        while (lenB > lenA) {
            itB = itB->next;
            lenB--;
        }
        
        // now, if we move them at the same pace, they will eventually reach the intersection (or NULL if none): O(min(m,n))
        while (itA != itB && itA != NULL /*&& itB != NULL*/) {
            itA = itA->next;
            itB = itB->next;
        }
        return itA;
    }
};
