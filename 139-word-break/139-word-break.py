class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        max_word, min_word = -1, float('inf')
        for word in words:
            max_word = max(len(word), max_word)
            min_word = min(len(word), min_word)
        if s in words:
            return True
        dp = [False for _ in range(len(s) + 1)]
        for end in range(1, len(s) + 1):
            first_idx = max(1, end - max_word)
            last_idx = min(end, end - min_word + 1)
            if s[:end] in words:
                dp[end] = True
            else:
                for start in range(first_idx, last_idx):
                    ending_word = s[start: end]
                    if ending_word not in words:
                        continue
                    if dp[start]:
                        dp[end] = True
                        break
            dp[end] = dp[end] or False
        return dp[-1]