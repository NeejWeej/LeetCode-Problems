# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth_nodes = {}
        cur = head
        num = 1
        while cur:
            nth_nodes[num] = cur
            cur = cur.next
            num += 1
        last_node = num - 1
        node_to_remove = 1 + last_node - n
        if node_to_remove == 1:
            return head.next
        before_node = nth_nodes.get(node_to_remove - 1)
        before_node.next = nth_nodes.get(node_to_remove + 1, None)
        return head