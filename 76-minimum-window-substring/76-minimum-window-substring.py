class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        
        bestS, bestE = 0, m
        
        start = 0
        
        tCounter = Counter(t)
        count = len(tCounter)
        counter = {}
        
        for i,v in enumerate(s):
            counter[v] = counter.get(v, 0) + 1
            if counter.get(v) == tCounter.get(v):
                count -= 1
            
            if count == 0:
                while counter.get(s[start], 0) > tCounter.get(s[start], -1):
                    oldVal = counter.pop(s[start], 0)
                    if oldVal > 1:
                        counter[s[start]] = oldVal - 1
                    start += 1
                
                if bestE - bestS > i - start:
                    bestE, bestS = i, start
        
        return s[bestS: bestE + 1] if bestE < m else ""
        
        