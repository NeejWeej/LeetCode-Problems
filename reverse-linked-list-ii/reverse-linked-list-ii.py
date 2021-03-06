# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        dummy = ListNode(0, head)
        idx = 0
        leftn = rightn = None
        cur = dummy
        while idx < left - 1:
            idx += 1
            cur = cur.next
        leftn = cur.next
        pre_left = cur
        while idx < right:
            idx += 1
            cur = cur.next
        rightn = cur
        
        pre_left.next = rightn
        temp = leftn.next
        leftn.next = rightn.next
        last = leftn
        while temp != rightn:
            temp2 = temp.next
            temp.next = last
            last = temp
            temp = temp2     
        temp.next = last
        return dummy.next
        
        
        
        
        # if left == right:
        #     return head
        # count = 1
        # curr = head
        # next_n = None
        # prev = None
        # prev_l = None
        # aft_r = None
        # while curr:
        #     if count == left - 1:
        #         prev_l = curr
        #     elif count == right + 1:
        #         aft_r = curr
        #     prev = curr
        #     curr = curr.next
        #     count += 1
        # count = 1
        # curr = head
        # while count < right:
        #     next_n = curr.next
        #     if count == left:
        #         curr.next = aft_r
        #     if count > left:
        #         curr.next = prev
        #     prev = curr
        #     curr = next_n
        #     count += 1
        # if prev_l:
        #     prev_l.next = curr
        # curr.next = prev
        # if left != 1:
        #     return head
        # else:
        #     return curr