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
private:
    int listLen = 0;
    ListNode* listHead = nullptr;
public:
    Solution(ListNode* head) {
        this->listHead = head;
        ListNode* it = head;
        while (it != nullptr) {
            it = it->next;
            this->listLen++;
        }
    }
    
    int getRandom() {
        std::random_device rd;  // Will be used to obtain a seed for the random number engine
        std::mt19937 gen(rd()); // Standard mersenne_twister_engine seeded with rd()
        std::uniform_int_distribution<> distrib(0, this->listLen - 1);
        int randomIndex = distrib(gen);
        ListNode* it = this->listHead;
        for (int i = 0; i < randomIndex; i++) {
            it = it->next;
        }
        return it->val;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
 