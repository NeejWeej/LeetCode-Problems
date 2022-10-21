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
    void reorderList(ListNode* head) {
        map<int, ListNode*> mp;
        int counter {0};
        ListNode* cur {head};
        while (cur){
            mp[counter++] = cur;
            cur = cur->next;
        }
        bool odd {counter % 2 == 1};
        int n {counter - 1};
        int start = 0;
        int end = n;
        while (start < end){
            mp[start++]->next = mp[end];
            if (end <= start){
                mp[end]->next = nullptr;
                break;
            }
            mp[end]->next = mp[start];
            end--;
        }
        if (odd) mp[start]->next = nullptr;
    }
};