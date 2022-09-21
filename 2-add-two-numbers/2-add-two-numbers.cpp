/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1->val == 0 && !l1->next) return l2;
        if (l2->val == 0 && !l2->next) return l1;
        
        ListNode* cur1 = l1;
        ListNode* cur2 = l2;
        ListNode* cur = new ListNode();
        ListNode* head = cur;
        int carry = 0;
        
        while (cur1 || cur2){
            cur->next = new ListNode();
            cur = cur->next;
            
            int newDigit = carry;
            if (cur1){
                newDigit += cur1->val;
                cur1 = cur1->next;
            }
            
            if (cur2){
                newDigit += cur2->val;
                cur2 = cur2->next;
            }
            cur->val = newDigit % 10;
            carry = newDigit / 10;
            
        }
        if(carry == 1) cur->next = new ListNode(1);
        ListNode* ans = head->next;
        delete head;
        return ans;
        
    }
};