# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursiveSwap(self, cur):
        next_node = cur.next
        if not next_node or not next_node.next:
            return None  
        cur.next = next_node.next
        cur = cur.next
        two_nodes_out = cur.next
        cur.next = next_node
        next_node.next = two_nodes_out
        return next_node
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head
        
        while cur:
            cur = self.recursiveSwap(cur)
            
        return dummy_head.next
        
        
#         if not head or not head.next:
#             return head
        
#         nodes = {}
#         idx = 0
#         cur = head
#         while cur:
#             nodes[idx] = cur
#             idx += 1
#             cur = cur.next
        
#         for i in range(0, idx + 1, 2):
#             if nodes[i].next = None:
#                 break
            
        
#         return nodes.get(1)
        
        