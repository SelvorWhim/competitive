# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_out_head = ListNode(0, None)
        l_out_ptr = l_out_head
        carry = 0
        while l1 and l2:
            digit = (l1.val + l2.val + carry) % 10
            carry = 1 if l1.val + l2.val + carry >= 10 else 0
            l_out_ptr.next = ListNode(digit, None)
            l_out_ptr = l_out_ptr.next
            l1 = l1.next
            l2 = l2.next
        remaining_l = l1 if l1 else l2
        while remaining_l:
            digit = (remaining_l.val + carry) % 10
            carry = 1 if remaining_l.val + carry >= 10 else 0
            l_out_ptr.next = ListNode(digit, None)
            l_out_ptr = l_out_ptr.next
            remaining_l = remaining_l.next
        if carry:
            l_out_ptr.next = ListNode(carry, None)
        return l_out_head.next
