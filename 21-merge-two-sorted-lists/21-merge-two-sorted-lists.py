# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = list1

        
        if not list1: return list2
        
        tail = dummy
        
        while list1:
            
            if list2 and list2.val < list1.val:
                tail.next, tail, list2 = list2, list2, list2.next
            
            else:
                tail.next, tail, list1 = list1, list1, list1.next
            
            if list2:
                list1, list2 = list2, list1
        
        return dummy.next
                
                
        