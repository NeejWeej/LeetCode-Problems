class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        idx = 0
        n = len(s)
        repeat = 0
        
        def decodeNum(s, idx):
            num = 0
            while s[idx].isdigit():
                num *= 10
                num += int(s[idx])
                idx += 1
            return num, idx
            
        
        def recursiveDecode(s, idx, count):
            repeat = 0
            ans = []
            while idx < len(s):
                if s[idx].isdigit():
                    repeat, idx = decodeNum(s, idx)
                elif s[idx] == '[':
                    toAdd, idx = recursiveDecode(s, idx + 1, repeat)
                    ans += toAdd
                elif s[idx] == "]":
                    idx += 1
                    return ans * count, idx
                else:
                    ans.append(s[idx])
                    idx += 1
            return None
        
        while idx < n:
            if s[idx].isdigit():
                repeat, idx = decodeNum(s, idx)  
            elif s[idx] == '[':
                toAdd, idx = recursiveDecode(s, idx + 1, repeat)
                res += toAdd
            else:
                res.append(s[idx])
                idx += 1
        return "".join(res)
        