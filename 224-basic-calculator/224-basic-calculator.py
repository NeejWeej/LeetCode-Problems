class Solution:
    
    def combine(self, overall, val, pos):
        if pos:
            overall += val
        else:
            overall -= val
        return overall
            
    def in_paren(self, s, idx):
        #starts after paren
        cur_num = 0
        overall_num = 0
        pos = True
        while idx < len(s):
            char = s[idx]
            if char.isdigit():
                cur_num *= 10
                cur_num += int(char)
            elif char == '(':
                val, new_idx = self.in_paren(s, idx + 1)[:]
                idx = new_idx
                overall_num = self.combine(overall_num, val, pos)
            elif char == '+':
                overall_num = self.combine(overall_num, cur_num, pos)
                pos = True
                cur_num = 0
            elif char == '-':
                overall_num = self.combine(overall_num, cur_num, pos)
                pos = False
                cur_num = 0
            elif char == ')':
                overall_num = self.combine(overall_num, cur_num, pos)
                cur_num = 0
                break
            idx += 1
        if cur_num != 0:
            overall_num = self.combine(overall_num, cur_num, pos)
        return [overall_num, idx]                
         
    def calculate(self, s: str) -> int:
        return self.in_paren(s, 0)[0]
                