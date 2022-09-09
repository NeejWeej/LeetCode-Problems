class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccur = {}
        n = len(s)
        for idx, c in enumerate(reversed(s)):
            i = n - idx - 1
            if c not in lastOccur:
                lastOccur[c] = i
        
        start = 0
        end = 0
        ans = []
        
        for i,c in enumerate(s):
            end = max(end, lastOccur.get(c, 0))
            if end == i:
                ans.append(end - start + 1)
                start = end + 1
        
        if start != n:
            ans.append(n - start)
        
        return ans
                