class Solution:
    from collections import defaultdict
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        heights = defaultdict(list)
        # heights = {0:0 for _ in range(n)}
        e = defaultdict(list)
        connections = defaultdict(int)
        for a,b in edges:
            e[a].append(b)
            e[b].append(a)
            connections[a] += 1
            connections[b] += 1
        start = set([x for x,i in connections.items() if i == 1])
        layer = start
        while layer:
            nl = set()
            if len(layer) == 1:
                return layer
            for x in layer:
                for y in e[x]:
                    if y in layer:
                        return list(layer)
                    if y in connections:
                        connections[y] -= 1
                        if connections.get(y) == 1:
                            nl.add(y)
            for x in layer:
                del connections[x]
            layer = nl
            
            