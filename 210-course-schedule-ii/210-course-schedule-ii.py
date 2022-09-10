class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = collections.defaultdict(int)
        isPreq = collections.defaultdict(list)
        for a,b in prerequisites:
            isPreq[b].append(a)
            preqs[a] += 1
        
        q = []
        for n in range(numCourses):
            if preqs.get(n, 0) == 0:
                q.append(n)
        
        ans = []
        while q:
            nc = q.pop()
            ans.append(nc)
            for p in isPreq[nc]:
                preqs[p] -= 1
                if preqs.get(p, 0) == 0:
                    q.append(p)
        
        return ans if len(ans) == numCourses else []
        