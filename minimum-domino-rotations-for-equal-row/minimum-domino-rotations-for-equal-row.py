class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top = tops
        bot = bottoms
        
        if len(tops) == 1:
            return 0
        dp = [({}, {}) for i in range(len(tops))]
        
        if top[0] == bot[0]:
            dp[0] = ({top[0]:0}, {bot[0]: 0})
            
        else:
            dp[0] = ({top[0]: 0, bot[0]: 1}, {top[0]: 1, bot[0]: 0})
        #each dp has a pair of
        
        for i in range(1, len(tops)):
            last = dp[i - 1]
            top_row = last[0]
            bot_row = last[1]
            
            if len(top_row) == 0 and len(bot_row) == 0:
                return -1
            
            new_top = {}
            new_bot = {}
            
            for k,v in top_row.items():
                if top[i] == k:
                    new_top[k] = v
                
                elif bot[i] == k:
                    new_top[k] = v + 1
                    
            for k,v in bot_row.items():
                if bot[i] == k:
                    new_bot[k] = v
                
                elif top[i] == k:
                    new_bot[k] = v + 1
                    
            dp[i] = (new_top, new_bot)
            
        # print(dp[-1][0].items(),dp[-1][1].items())
        
        min_count = float('inf')
        
        for count in dp[-1][0].values():
            if count < min_count:
                min_count = count
                
        for count in dp[-1][1].values():
            if count < min_count:
                min_count = count
        
        return min_count
        #min num flips to make top x, or bot y 
        # self.minDominoRotations(tops[1:], bot[1:])
        