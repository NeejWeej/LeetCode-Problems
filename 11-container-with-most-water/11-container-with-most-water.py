class Solution:     
#     def volume(self, height, left, right):
#         return abs(left-right)*min(height[left],height[right])
    
#     def rec_area(self, height):
#         if len(height)==2:
#             return min(height[0],height[1])
#         l = 0
#         r = len(height)-1
#         vol = self.volume(height,l,r)
#         if height[l]<=height[r]:
#             return max(vol, self.rec_area(height[1:]))
#         if height[l]>height[r]:
#             return max(vol, self.rec_area(height[:-1]))
        
        
    def maxArea(self, height: List[int]) -> int: 
        best = 0
        start = 0
        end = len(height) - 1
        while start < end:
            start_height = height[start]
            end_height = height[end]
            best = max(best, min(start_height, end_height) * (end - start))
            if start_height == end_height:
                start += 1
                end -= 1
            elif start_height < end_height:
                start += 1
            else:
                end -= 1
        return best
                
            