class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maL = {}
        for c in magazine:
            maL[c] = maL.get(c, 0) + 1
        rn = {}
        for c in ransomNote:
            if c not in maL:
                return False
            rn[c] = rn.get(c, 0) + 1
        for c, count in rn.items():
            if maL.get(c, 0) < count:
                return False
        return True