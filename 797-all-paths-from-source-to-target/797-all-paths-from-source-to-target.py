class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        n = len(graph)
        
        def dfs(path, curnode):
            path.append(curnode)
            if curnode == n - 1:
                self.ans.append(path[:])
                
            for child in graph[curnode]:
                dfs(path, child)
            path.pop()
            
        dfs([], 0)
        return self.ans