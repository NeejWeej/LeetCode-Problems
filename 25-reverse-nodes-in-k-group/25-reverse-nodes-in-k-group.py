# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(whats_next, start, end):
            cur = start
            prev = whats_next
            while cur != end:
                nextt = cur.next
                cur.next = prev
                cur, prev = nextt, cur
            nextt = cur.next
            cur.next = prev
            return [end, start]
        
        dummy = ListNode(0, head)
        start = head
        prev = dummy
        while start:
            counter = 1
            cur = start
            while counter < k:
                if not cur:
                    return dummy.next
                cur = cur.next
                counter += 1
            if not cur:
                return dummy.next
            nextt = cur.next
            start_of_group, end_of_group = reverse(nextt, start, cur)
            prev.next = start_of_group
            start = nextt
            prev = end_of_group
        return dummy.next
        