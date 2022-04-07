# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while slow.next and fast and fast.next:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        return slow