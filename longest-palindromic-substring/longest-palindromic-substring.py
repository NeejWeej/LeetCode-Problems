class Solution:     
    def longestPalindrome(self, s: str) -> str:
        centers = 2 * len(s)
        best = 1
        pali = s[0]
        for i in range(centers):
            cur_substr = ''
            if i % 2 == 0:
                #between letters
                idx = (i + 1)//2
                start = idx
                end = idx + 1
                while 0 <= start and end <= len(s) - 1 and s[start] == s[end]:
                    start -= 1
                    end += 1
                cur_substr = s[start + 1: end]
                cur_len = len(cur_substr)
                if cur_len > best:
                    pali = cur_substr
                    best = cur_len
            
            elif i % 2 == 1:
                idx = i//2
                start = idx
                end = idx
                while 0 <= start and end <= len(s) - 1 and s[start] == s[end]:
                    start -= 1
                    end += 1 
                cur_substr = s[start + 1: end]
                cur_len = len(cur_substr)
                if cur_len > best:
                    pali = cur_substr
                    best = cur_len       
            # print(i, cur_substr)
        return pali