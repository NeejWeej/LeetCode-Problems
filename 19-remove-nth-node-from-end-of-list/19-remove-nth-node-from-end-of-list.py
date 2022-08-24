# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        d = {0: dummy}
        counter = 1
        cur = head
        while cur:
            d[counter] = cur
            counter += 1
            cur = cur.next
            
        beforeRemove = d.get(counter - n - 1)
        beforeRemove.next = beforeRemove.next.next
        
        return dummy.next