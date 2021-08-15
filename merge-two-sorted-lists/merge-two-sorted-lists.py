# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        start = next_l1 = next_l2 = None
        if l1.val <= l2.val:
            start = l1
            next_l1 = l1.next
            next_l2 = l2
        else:
            start = l2
            next_l1 = l1
            next_l2 = l2.next            
        curr = start
        while next_l1 is not None or next_l2 is not None:
            if next_l1 is None:
                curr.next = next_l2
                next_l2 = next_l2.next
            elif next_l2 is None:
                curr.next = next_l1
                next_l1 = next_l1.next
            elif next_l1.val <= next_l2.val:
                curr.next = next_l1
                next_l1 = next_l1.next
            else:
                curr.next = next_l2
                next_l2 = next_l2.next
            curr = curr.next
        return start
                