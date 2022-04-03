class Solution:
    def in_paren(self, stack, s, idx):
        #starts after paren
        new_stack = []
        cur_num = 0
        while idx < len(s):
            char = s[idx]
            if char.isdigit():
                cur_num *= 10
                cur_num += int(char)
            elif char == '(':
                new_idx = self.in_paren(new_stack, s, idx + 1)
                idx = new_idx
                cur_num = 0
            elif char == '+':
                if cur_num != 0:
                    new_stack.append(cur_num)
                new_stack.append('+')
                cur_num = 0
            elif char == '-':
                if cur_num != 0:
                    new_stack.append(cur_num)
                new_stack.append('-')
                cur_num = 0
            elif char == ')':
                if cur_num != 0:
                    new_stack.append(cur_num)
                cur_num = 0
                break
            idx += 1
        if cur_num != 0:
            new_stack.append(cur_num)
        # print(new_stack)
        ans = 0
        pos = True
        for val in new_stack:
            if val == '+':
                pos = True
            elif val == '-':
                pos = False
            else:
                if pos:
                    ans += val
                else:
                    ans -= val
        stack.append(ans)
        return idx                
         
    def calculate(self, s: str) -> int:
        stack = []
        self.in_paren(stack, s, 0)
        return stack[0]
                