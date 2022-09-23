class Solution {
public:
    
    static bool comparePos(tuple<int,int> i1, tuple<int,int> i2)
    {
        return (get<0>(i1) > get<0>(i2));
    }
    
    double destTime(const int target, const tuple<int, int>& car){
        return double(target - get<0>(car)) / double(get<1>(car));
    }
  
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<tuple<int,int>>sp(0);
        int ans = 0;
        
        for(int i = 0; i < speed.size(); ++i){
            sp.push_back({position[i], speed[i]});
        }
        
        sort(sp.begin(), sp.end(), Solution::comparePos);
        
        vector<double> stack;
        
        stack.push_back(destTime(target, sp[0]));
        
        for(auto& car: sp){
            double arrival = destTime(target, car);
            // cout<< arrival << " " << stack.back() << "\n";
            if (arrival > stack.back()) stack.push_back(arrival);
        }
        // cout<<"\n";
        // for(auto& p: sp) cout<< get<0>(p) << ","<< get<1>(p) << " ";
        // cout << "\n";
        // for(auto t: stack) cout<< t<< " ";
        
        return stack.size();
    }
};