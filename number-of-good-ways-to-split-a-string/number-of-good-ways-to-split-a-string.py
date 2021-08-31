class Solution:
    def numSplits(self, s: str) -> int:
        distinct_letters = set()
        ul = [0] * len(s)
        count = 0
        for idx, char in enumerate(s):
            if char not in distinct_letters:
                distinct_letters.add(char)
                count += 1
            ul[idx] = count
        
        other_way = [0] * len(s)
        distinct_letters= set()
        count = 0
        for idx, char in enumerate(reversed(s)):
            if char not in distinct_letters:
                distinct_letters.add(char)
                count += 1
            other_way[idx] = count
        ans = 0
        for idx, val in enumerate(ul[:-1]):
            if other_way[ -idx - 2] == val:
                ans += 1
        return ans
            
        