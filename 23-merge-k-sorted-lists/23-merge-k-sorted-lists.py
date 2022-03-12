# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        start = [(x.val, idx, x) for idx, x in enumerate(lists) if x]
        counter = len(lists)
        hq.heapify(start)
        dummy = ListNode()
        cur = dummy
        while len(start) > 0:
            useless_val, idx, nextt = hq.heappop(start)[:]
            cur.next = nextt
            cur = nextt
            if nextt.next:
                nextt = nextt.next
                hq.heappush(start, (nextt.val, counter + 1, nextt))
                counter += 1
        return dummy.next