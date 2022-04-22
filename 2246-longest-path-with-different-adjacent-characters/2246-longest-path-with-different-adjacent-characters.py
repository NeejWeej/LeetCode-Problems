class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        lp = 0
        kids = {}
        for i, p in enumerate(parent):
            if p == -1 or s[p] == s[i]:
                continue
            kids[p] = kids.get(p, {'c': 0, 'k': []})
            kp = kids.get(p)
            kp.get('k').append(i)
            kp['c'] += 1
        start = []
        for n in range(len(parent)):
            if n not in kids or kids.get(n).get('c') == 0:
                start.append(n)
        h = {}
        while start:
            next_layer = []
            for cur in start:
                first_long = 0
                second_long = 0
                for kid in kids.get(cur, {}).get('k', []):
                    height = h.get(kid, 0)
                    second_long = max(second_long, height)
                    if first_long < second_long:
                        first_long, second_long = second_long, first_long
                lp = max(lp, first_long + second_long)
                h[cur] = first_long + 1
                p = parent[cur]
                if p == -1 or (s[p] == s[cur]):
                    continue
                kids.get(p)['c'] -= 1
                if kids.get(p).get('c') == 0:
                    next_layer.append(p)
            start = next_layer
        return lp + 1