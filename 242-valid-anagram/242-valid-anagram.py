from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(Counter(s).items()) == sorted(Counter(t).items())