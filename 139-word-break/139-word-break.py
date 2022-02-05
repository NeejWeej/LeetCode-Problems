class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        if s in words:
            return True
        dp = [False for _ in range(len(s) + 1)]
        if s[0] in words:
            dp[0] = True
            
        for end in range(1, len(s) + 1):
            if s[:end] in words:
                dp[end] = True
            else:
                for start in range(1, end):
                    ending_word = s[start: end]
                    if ending_word not in words:
                        continue
                    if dp[start]:
                        dp[end] = True
                        break
            dp[end] = dp[end] or False
        return dp[-1]
#     def set_wordBreak(self, s, words, seen):
#         if seen.get(s, False):
#             return True
#         # print(seen)
#         for end in range(1, len(s)):
#             substr = s[:end] 
#             if not seen.get(substr, False):
#                 continue
#             rest = self.set_wordBreak(s[end:], words, seen)
#             if rest:
#                 seen[s] = True
#                 return True
#         seen[s] = False
#         return False
        
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         words = set(wordDict)
#         seen = {word: True for word in wordDict}
#         letters = {c for word in wordDict for c in word}
#         for char in s:
#             if char not in letters:
#                 return False
#         return self.set_wordBreak(s, words, seen)