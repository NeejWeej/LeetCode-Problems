# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mapp = {}
        
        cur = head
        val = 0
        
        while cur:
            mapp[val] = cur
            cur = cur.next
            val += 1
        val -= 1
        start = 0
        
        while start <= val // 2:
            mapp[start].next= mapp[val - start]
            if start + 1 <= val // 2:
                mapp[val - start].next = mapp[start + 1]
            else:
                mapp[val - start].next = None
            start += 1
        
        return head
        