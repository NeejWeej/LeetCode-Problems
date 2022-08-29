# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        dummy = ListNode(val=0)
        dummy.next = head
        
        end = None
        headOfLast = None
        cur = dummy
        
        while cur:
            headOfLast = cur
            for _ in range(k):
                if not cur:
                    return dummy.next
                cur = cur.next
                
            if not cur:
                return dummy.next
            
            # end is last node in group
            end = cur
            firstInGroup = headOfLast.next
            prev = firstInGroup
            cur = prev.next
            
            while cur != end:
                nextVal = cur.next
                cur.next = prev
                prev = cur
                cur = nextVal
            # have to adjust end too   
            firstInGroup.next = end.next
            cur.next = prev
            
            headOfLast.next = end
            cur = firstInGroup
        