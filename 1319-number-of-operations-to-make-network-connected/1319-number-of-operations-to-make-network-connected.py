class Solution:
    from collections import defaultdict
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(g, cur, visited, info):
            info[0] += 1
            visited.add(cur)
            neighs = g.get(cur, [])
            info[1] += len(neighs)
            for x in neighs:
                if x not in visited:
                    dfs(g, x, visited, info)
            return info
        graph = defaultdict(set)
        for a,b in connections:
            graph[a].add(b)
            graph[b].add(a)
        available = 0
        groups = []
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            new = i
            size, connect = dfs(graph, i, visited, [0, 0])
            groups.append((size, connect // 2))
        # print(groups)
        extra = 0 
        for a,b in groups:
            extra += (b - a + 1)
        diff = len(groups) - extra
        return len(groups) - 1 if diff <= 1 else -1