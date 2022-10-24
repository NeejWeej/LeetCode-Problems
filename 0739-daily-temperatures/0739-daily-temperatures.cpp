struct tempIdx {
    int temp;
    int idx;
    
    tempIdx(int t, int i): temp(t), idx(i) {}
};

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n, 0);
        
        vector<tempIdx> data;
        int counter = 0;
        for(int idx = 0; idx<n; ++idx){
            int temp = temperatures[idx];
            while(data.size() > 0){
                tempIdx& end = data.back();
                if (end.temp >= temp){
                    break;
                }
                res[end.idx] = (idx - end.idx);
                data.pop_back();
            }
            data.emplace_back(temp, idx);
        }
        return res;
    }
};