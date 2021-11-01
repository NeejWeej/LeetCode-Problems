# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        cur = head.next
        head.next = None
        while cur:
            next_cur = cur.next
            cur.next = None
            start = dummy_head
            while start.next and cur.val >= start.next.val:
                start = start.next
            if start.next:
                temp = start.next
                start.next = cur
                cur.next = temp
            else:
                start.next = cur
            cur = next_cur
        
        return dummy_head.next