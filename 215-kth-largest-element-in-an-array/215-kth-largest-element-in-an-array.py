class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick(count, vals):
            left = []
            right = []
            equal = []
            
            key = random.choice(vals)
            
            for val in vals:
                if val < key:
                    left.append(val)
                elif val == key:
                    equal.append(val)
                else:
                    right.append(val)
            
            if len(right) < count:
                if len(right) + len(equal) >= count:
                    return key
                else:
                    return quick(count - len(right) - len(equal), left)
            
            else:
                return quick(count, right)
        
        return quick(k, nums)
            
                
            
                