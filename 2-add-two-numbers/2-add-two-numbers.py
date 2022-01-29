# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_cur = l1
        l2_cur = l2
        carry = 0
        
        new_node = ListNode()
        start = new_node
        prev_node = None
        while l1_cur is not None or l2_cur is not None:
            l1_cur_val = l2_cur_val = 0
            if l1_cur:
                l1_cur_val = l1_cur.val
            if l2_cur:
                l2_cur_val = l2_cur.val
            new_val = l1_cur_val + l2_cur_val + carry
            if new_val >= 10:
                carry = 1
                new_val -= 10
            else:
                carry = 0
            new_node.val = new_val
            if prev_node:
                prev_node.next = new_node
            prev_node = new_node
            new_node = ListNode()
            if l1_cur:
                l1_cur = l1_cur.next
            if l2_cur:
                l2_cur = l2_cur.next
        if carry == 1:
            new_node = ListNode(1)
            prev_node.next = new_node
        return start
        
        
        