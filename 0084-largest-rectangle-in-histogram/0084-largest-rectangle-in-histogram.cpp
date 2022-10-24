struct rect{
    int i;
    int h;
    
    rect(int i, int h): i(i), h(h) {};  
};

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector<rect> deq;
        deq.emplace_back(-1, INT_MAX);
        heights.push_back(INT_MIN);
        int n = heights.size();
        int best = INT_MIN;
        for(int i = 0; i < n; i++){
            int& h = heights[i];
            while(h < deq.back().h){
                int j = deq.size();
                // index of last is j - 1
                if (j == 1) break;
                best = max(best, deq[j-1].h * (i - deq[j - 2].i - 1) );
                deq.pop_back();
            }
            if (h == deq.back().h) deq.back().i = i;
            else deq.emplace_back(i, h);
        }
        return best;
    }
};