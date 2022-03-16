class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        last = 1
        last2 = 1
        can_have = set(['1','2'])
        can_have_2 = set(['0','1', '2','3', '4', '5','6'])
        for idx in range(1, len(s)):
            if s[idx] == '0':
                if s[idx - 1] not in can_have:
                    return 0
                else:
                    last, last2 = last2, last
            else:
                cur = last
                if s[idx - 1] == '1':
                    cur += last2
                elif s[idx - 1] == '2' and s[idx] in can_have_2:
                    cur += last2
                last, last2 = cur, last
        return last
    
        