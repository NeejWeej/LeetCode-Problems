class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = []
        start_idx = 0
        def go_up_diagonal(s, idx):
            start = -2
            while start > -numRows and idx< len(s):
                res.append([0]*numRows)
                res[-1][start] = s[idx]
                start -=1
                idx += 1
            return idx
        def full_column(s, idx):
            stop_idx = min(numRows+ idx, len(s))
            res.append(s[idx:stop_idx])
            idx = stop_idx
            return idx
        while start_idx < len(s):
            start_idx = full_column(s, start_idx)
            start_idx = go_up_diagonal(s, start_idx)
        
        res[-1] += '0'*(numRows - len(res[-1]))
        # while len(res[-1]) < numRows:
        #     res[-1].append(0)
        # print(res)
        cur_idx = 0
        ans = []
        while cur_idx < numRows:
            for i in range(len(res)):
                if res[i][cur_idx] != 0 and res[i][cur_idx] != '0':
                    ans.append(res[i][cur_idx])
            cur_idx += 1
        return "".join(ans)
        
        