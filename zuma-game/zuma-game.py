class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        min_balls = float('inf')
        
#         colors_in_hand = {}
        
#         for c in hand:
#             colors_in_hand[c] = colors_in_hand.get(c, 0) + 1

        @lru_cache(None) 
        def clearBoard(b):
            if len(b) < 3:
                return b
            
            ans = []
            prev_char = None
            for char in b:
                if len(ans) < 3:
                    ans.append(char)
                    prev_char = char
                    continue
                
                not_prev = prev_char != char
                last_two = ans[-3] == prev_char and ans[-1] == prev_char
                last_three = last_two and ans[-2] == prev_char
                
                if not_prev and last_three:
                    ans.pop()
                    ans.pop()
                    while len(ans) > 0 and ans[-1] == prev_char:
                        ans.pop()
                    ans.append(char)
                    prev_char = char
                    continue
                    
                ans.append(char)
                prev_char = char
            
            if len(ans) >= 3 and ans[-1] == ans[-2] and ans[-2] == ans[-3]:
                char = ans[-1]
                while len(ans) > 0 and ans[-1] == char:
                    ans.pop()
            return ''.join(ans)
            
            
        @lru_cache(None)   
        def dfs(bd, hd, count):
            nonlocal min_balls
            if len(bd) == 0 and count < min_balls:
                min_balls = count
            
            if len(hd) == 0:
                return
            
            for idx, ball in enumerate(hd):
                new_hd = hd[:idx] + hd[idx +1: ]
                for i in range(len(bd)):
                    new_bd = bd[:i] + ball + bd[i:]
                    temp_bd = clearBoard(new_bd)
                    # if temp_bd != new_bd:
                    #     print(new_bd, temp_bd, new_hd, hd)
                    new_bd = temp_bd
                    dfs(new_bd, new_hd, 1 + count)
        
        dfs(board, hand, 0)
            
            
#         def backtrack(bd, hd, count):
#             nonlocal min_balls
            
#             if bd == '':
#                 if count < min_balls:
#                     min_balls = count
#                 return
            
#             if len(hd) == 0:
#                 return
#             for color in hd.keys():
#                 last_sighting = -1
#                 do_we_need_it = True
                
#                 for idx in range(len(bd)):
#                     new_bd = bd[:idx] + color + bd[idx:]
                    
#                     if len(new_bd) >= 3:
#                         left = False
#                         if idx != 0:
#                             left = left or (bd[idx - 1] == color)
                        
#                         right = False
#                         if idx != len(bd) - 1:
#                             right = right or (bd[idx + 1] == color)
                        
#                         if left or right:
#                             new_bd = clearBoard(new_bd)
#                     new_hd = {k:v for k,v in hd.items()}

#                     new_hd[color] -= 1
#                     if new_hd.get(color) == 0:
#                         del new_hd[color]
#                     backtrack(new_bd, new_hd, count + 1)
#                     if bd[idx] == color:
#                         last_sighting = idx

#                     if bd[idx: idx + 2] == color + color:
#                         do_we_need_it = False
#                         new_bd = bd[:idx] + color + bd[idx:]

#                         new_bd = clearBoard(new_bd)

#                         new_hd = {k:v for k,v in hd.items()}

#                         new_hd[color] -= 1
#                         if new_hd.get(color) == 0:
#                             del new_hd[color]
#                         backtrack(new_bd, new_hd, count + 1)
                    
#                 if do_we_need_it:
#                     new_bd = bd[:last_sighting] + color + bd[last_sighting:]
#                     new_bd = clearBoard(new_bd)
#                     new_hd = {k:v for k,v in hd.items()}
#                     new_hd[color] -= 1
#                     if new_hd.get(color) == 0:
#                         del new_hd[color]
#                     backtrack(new_bd, new_hd, count + 1) 
                    
        # backtrack(board, colors_in_hand, 0)
        # print('WWWRRBBWW', clearBoard('WWWRRBBWW'))
        return -1 if min_balls == float('inf') else min_balls
            