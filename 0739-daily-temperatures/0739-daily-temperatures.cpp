class Solution {
    
struct tempIdx {
    int temp;
    int idx;
    
    tempIdx(int t, int i): temp(t), idx(i) {}
};
    
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n, 0);
        
        vector<tempIdx> data;
        int counter = 0;
        while(counter < n){
            int idx = counter;
            int temp = temperatures[counter];
            ++counter;
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