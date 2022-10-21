/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* cur = head;
        if(!head) return nullptr;
        
        map<Node*, Node*>mp;
        mp[nullptr] = nullptr;
        mp[head] = new Node(head->val);
        while(cur){
            if (mp.find(cur->next) == mp.end()){
                mp.insert({cur->next, new Node(cur->next->val)});
            }
            mp[cur]->next = mp[cur->next];
            Node* rand = cur->random;
            if (mp.find(rand) == mp.end()){
                mp.insert({rand, new Node(rand->val)});
            }
            mp[cur]->random = mp[rand];
            cur = cur->next;
        }
        return mp[head];
    }
};