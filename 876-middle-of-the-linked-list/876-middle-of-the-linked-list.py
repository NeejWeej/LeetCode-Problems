# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        return slow