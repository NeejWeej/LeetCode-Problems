/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(!head || !head->next) return false;
        
        ListNode *slow = head->next, *fast = slow;
        fast = fast->next;
        
        while (fast){
            if (slow == fast){
                return true;
            }
            slow = slow->next;
            fast = fast->next;
            if(!fast) return false;
            fast = fast->next;
        }
        
        return false;
    }
};