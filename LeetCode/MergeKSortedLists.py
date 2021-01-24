# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ret_head_dummy = ListNode()
        ret_ptr = ret_head_dummy
        for i in reversed(range(len(lists))):
            if lists[i] is None:
                del lists[i]
        while len(lists) > 0:
            min_val = lists[0].val
            min_i = 0
            for i in range(1, len(lists)):
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    min_i = i
            ret_ptr.next = ListNode(min_val)
            ret_ptr = ret_ptr.next
            lists[min_i] = lists[min_i].next
            if lists[min_i] is None:
                del lists[min_i]
        return ret_head_dummy.next
