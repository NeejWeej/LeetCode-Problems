class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        start = 0
        end = len(s) - 1
        while True:
            if start == end:
                return True
            
            elif start + 1 == end and s[start] == s[end]:
                return True
            
            elif s[start] == s[end]:
                start += 1
                end -= 1
                continue
            else:
                if s[start: end] == s[start:end][::-1]:
                    return True
                if s[start + 1: end + 1] == s[start + 1: end + 1][::-1]:
                    return True
                return False
                
        # for i in range(len(s)):
        #     word = s[:i] + s[i+1:]
        #     if word == word[::-1]:
        #         return True
        # return False