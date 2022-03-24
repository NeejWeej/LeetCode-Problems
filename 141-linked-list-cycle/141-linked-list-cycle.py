# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while slow and fast:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
        