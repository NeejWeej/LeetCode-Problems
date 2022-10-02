class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = collections.deque([])
        n = len(arr)
        
        def binSearch(val):
            s = 0
            e = n - 1
            while s < e:
                mid = (s + e)//2
                curV = arr[mid]
                if curV < val:
                    s = mid + 1
                else:
                    e = mid
            return s
        
        def dist(val):
            return abs(val - x) if val is not None else float('inf')
        
        idx = binSearch(x)
        ans = collections.deque([arr[idx]])
        left = idx - 1
        right = idx + 1
        
        rightSide = arr[idx + 1: min(n, idx + 1 + k - 1)]
        leftSide = arr[max(0, idx - 1 - (k - 1)): idx + 1]
        
        ans = collections.deque(leftSide + rightSide)
        while len(ans) > k:
            leftV = ans[0]
            rightV = ans[-1]
            if dist(leftV) <= dist(rightV):
                ans.pop()
            else:
                ans.popleft()
            
        return ans
            
            
            
            
        