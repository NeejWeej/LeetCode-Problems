class Solution:
    def myAtoi(self, s: str) -> int:
        pos = 1
        i = -1
        for idx,c in enumerate(s):
            if c != " ":
                i = idx
                break
        if i == -1:
            return 0
        if s[i] in ["+", "-"]:
            if s[i] == '-':
                pos = -1
            i += 1
        lenOfDigits = -1
        end = len(s)
        for j in range(i, len(s)):
            if s[j].isdigit():
                lenOfDigits += 1
            else:
                end = j
                break
        ans = 0
        for j in range(i, end):
            ans += (10 ** lenOfDigits) * int(s[j])
            lenOfDigits -= 1
        ans *= pos
        if ans >= (1 << 31):
            ans = (1 << 31) - 1
        elif ans <= -(1<< 31):
            ans = -(1<< 31)
        return ans
        
            
        