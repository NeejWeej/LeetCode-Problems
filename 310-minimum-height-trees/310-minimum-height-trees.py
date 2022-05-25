class Solution:
    from collections import defaultdict
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        heights = defaultdict(list)
        # heights = {0:0 for _ in range(n)}
        e = defaultdict(set)
        for a,b in edges:
            e[a].add(b)
            e[b].add(a)
        start = set([x for x,i in e.items() if len(i) == 1])
        layer = start
        while layer:
            nl = set()
            if len(layer) == 1:
                return layer
            for x in layer:
                while e[x]:
                    y = e[x].pop()
                    if y in layer:
                        return layer
                    e[y].remove(x)
                    if len(e[y]) == 1:
                        nl.add(y)
                del e[x]
            layer = nl
            
            