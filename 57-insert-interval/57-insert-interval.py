class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = 0
        n = len(intervals)
        if n == 0:
            return [newInterval]
        # end = n - 1
        # insert_spot = -1
        
        ns, ne = newInterval[:]
        stack = []
        i = 0
        flag = True
        while i < n:
            s,e = intervals[i]
            if ns <= s and flag:
                flag = False
                s, e = ns, ne
                i -= 1
            
            if stack:
                last_s, last_e = stack.pop()[:]
                if (last_s <= s and s <= last_e) or (s <= last_s and last_s <= e):
                    new_s = min(s, last_s)
                    new_e = max(e, last_e)
                    stack.append([new_s, new_e])
                else:
                    stack.append([last_s, last_e])
                    stack.append([s, e])
            else:
                stack.append([s, e])
            i += 1
        if stack[-1][0] <= ns and flag:
            if ns <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], ne)
            else:
                stack.append([ns, ne])
        return stack
        
        
        
#         while start < end:
#             mid = start + (end - start) // 2
#             ts = intervals[mid][0]
#             if ts == ns:
#                 insert_spot = mid
#                 break
#             if ts < ns:
#                 start = mid + 1   
#             elif ts > ns:
#                 end = mid
        
#         if insert_spot == -1:
#             insert_spot = start
        
#         print(insert_spot)
#         end_collide = insert_spot - 1
#         for i in range(insert_spot, n):
#             if intervals[i][0] <= ns and ns <= intervals[i][1]:
#                 continue
#             if ns <= intervals[i][0] and intervals[i][0] <= ne:
#                 continue
#             end_collide = i
#             break
#         new_start = min(ns, intervals[insert_spot][0])
#         new_end = max(ne, intervals[end_collide][1])
#         print(end_collide, insert_spot)
#         for i in range(end_collide - 1, insert_spot - 2, -1):
#             del intervals[i]
#         intervals.insert(insert_spot, [new_start, new_end])
#         return intervals
        
            
        
        
        
            
        