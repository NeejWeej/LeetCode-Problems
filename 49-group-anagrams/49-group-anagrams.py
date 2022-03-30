           
class Solution:
   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            cur = {}
            for c in s:
                cur[c] = cur.get(c, 0) + 1
            run = tuple(sorted([(c, count) for c, count in cur.items()]))
            g = groups.get(run, [])
            g.append(s)
            groups[run] = g
        return groups.values()
        