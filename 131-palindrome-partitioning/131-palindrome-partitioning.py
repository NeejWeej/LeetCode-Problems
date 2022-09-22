class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n) ]
        dp[0].append([s[0]])
        
        
        for i in range(1, n):
            for st in range(i + 1):
                port = s[st: i + 1]
                if port == port[::-1]:
                    if st == 0:
                        dp[i].append([port])
                    elif dp[st - 1]:
                        for val in dp[st - 1]:
                            dp[i].append(val + [port]) 
        return dp[-1]