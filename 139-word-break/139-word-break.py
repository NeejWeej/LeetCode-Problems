class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n)]
        mod = 10**9 + 7
        prime = 31
        
        d = set(wordDict)
        
        checkPoints = [-1]
        for i,c in enumerate(s):
            for c in checkPoints:
                start = c + 1
                if s[start: i + 1] in d:
                    dp[i] = True
                    checkPoints.append(i)
                    break
        return dp[-1]