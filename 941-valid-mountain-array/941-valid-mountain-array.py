class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False
        
        start = 0
        last = float('-inf')
        while start < len(arr):
            if arr[start] == last:
                return False      
            if arr[start] < last:
                break
            last = arr[start]
            start += 1
            
        last = arr[start]
        start += 1 
        
        while start < len(arr):
            if arr[start] >= last:
                return False
            last = arr[start]
            start += 1
        
        return True
            
                