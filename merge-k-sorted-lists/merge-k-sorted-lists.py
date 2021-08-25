# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode()
        curr = ans
        pq = [(l.val, idx, l) for idx, l in enumerate(lists) if l]
        z = len(lists)
        heapq.heapify(pq)
        while pq:
            curr.next = heapq.heappop(pq)[-1]
            curr = curr.next
            if curr.next:
                heapq.heappush(pq, (curr.next.val, z, curr.next))
                z += 1         
        return ans.next