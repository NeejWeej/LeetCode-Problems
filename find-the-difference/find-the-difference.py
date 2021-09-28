class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char,0) + 1
        for char in t:
            if count.get(char, 0) <= 0:
                return char
            count[char] = count.get(char, 0) - 1
        