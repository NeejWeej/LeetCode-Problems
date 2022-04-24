class Solution:
    from collections import deque
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        if len(a) < len(b):
            a,b = b,a
        ans = deque([])
        for i in range(-1, -1 -len(b), -1):
            x1 = int(a[i])
            x2 = int(b[i])
            add = x1 + x2 + carry
            if add >= 2:
                carry = 1
            else:
                carry = 0
            add = add % 2
            ans.appendleft(str(add))
        
        for i in range(-1 -len(b), -1 - len(a), -1):
            x1 = int(a[i])
            x2 = 0
            add = x1 + x2 + carry
            if add >= 2:
                carry = 1
            else:
                carry = 0
            add = add % 2
            ans.appendleft(str(add))
        if carry == 1:
            ans.appendleft(str(carry))
        return "".join(ans)