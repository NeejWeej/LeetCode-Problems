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
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        available = 0
        groups = []
        visited = set()
        extra = 0 
        groups = 0
        for i in range(n):
            if i in visited:
                continue
            new = i
            groups += 1
            size, connect = dfs(graph, i, visited, [0, 0])
            connect //= 2
            extra += (connect - size + 1)
        diff = groups - extra
        return groups - 1 if diff <= 1 else -1