class Solution {
public:
    void dfs(vector<vector<char>>& grid, vector<pair<int, int>>& direc, int r, int c, int& m, int&n){
        grid[r][c] = '0';
        for(auto [dx, dy]: direc){
            if(0<=r+dx && r+dx<m && 0<=c+dy && c+dy<n && grid[r+dx][c+dy]=='1'){
                dfs(grid, direc, r+dx, c+dy, m, n);
            }
            
        }
        
    }
    
    int numIslands(vector<vector<char>>& grid) {
        int num = 0;
        int m = grid.size();
        int n = grid[0].size();
        vector<pair<int, int>> direc {{0,1}, {1,0}, {-1, 0}, {0, -1}};
        
        for(int r=0; r<m; ++r){
            for(int c=0; c<n; ++c){
                if(grid[r][c] == '1'){
                    ++num;
                    dfs(grid, direc, r, c, m, n);
                }
            }
        }
        
        return num;
        
        
    }
};