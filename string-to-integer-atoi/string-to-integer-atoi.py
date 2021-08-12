class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        list_s = s.strip()
        if len(list_s) == 0:
            return res
        idx = 0
        sign = 1
        if list_s[0] is '-':
            sign = -1
            idx += 1
        elif list_s[0] is '+':
            idx += 1
        while idx < len(list_s) and list_s[idx].isdigit():
            res *= 10
            res += ord(list_s[idx]) - ord('0')
            idx += 1
        res *= sign
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        return res
        