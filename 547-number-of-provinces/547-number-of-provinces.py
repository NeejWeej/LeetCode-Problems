class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        prov = 0
        seen = set()
        graph = defaultdict(set)
        
        n = len(isConnected)
        
        def search(cur):
            seen.add(cur)
            for neigh in range(n):
                if isConnected[cur][neigh] and neigh not in seen:
                    search(neigh)
        
        for i in range(n):
            if i not in seen:
                prov += 1
                search(i)
                
        return prov
            