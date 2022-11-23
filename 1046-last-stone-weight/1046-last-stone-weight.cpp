class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq {stones.begin(), stones.end()};
        while( pq.size() > 1){
            int x {pq.top()};
            pq.pop();
            int y {pq.top()};
            pq.pop();
            if (int val = x - y; val > 0) pq.push(val);
        }
        return pq.size() == 1? pq.top() : 0;
    }
};