# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if not head:
            return head
        while cur and cur.next:
            nextt = cur.next
            while nextt and nextt.val == cur.val:
                nextt = nextt.next
            cur.next = nextt
            cur = nextt
        return head