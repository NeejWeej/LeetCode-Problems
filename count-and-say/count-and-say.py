class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        last = self.countAndSay(n-1)
        
        count = 0
        val = 'a'
        
        ans = []
        for digit in last:
            if digit != val:
                if count != 0:
                    ans += [str(count), val] 
                val = digit
                count = 1
            else:
                count += 1
        ans += [str(count), val]
        return "".join(ans)
        
        
        # cur_str = [(1,1)]
        # for i in range(n):
        #     new_str = []
        #     for pair in cur_str:
        #         num, count = pair[0], pair[1]
        #         new_str += [count, num]
            
        