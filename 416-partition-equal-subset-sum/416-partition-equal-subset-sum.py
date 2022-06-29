class Solution: 
    def canPartition(self, nums: List[int]) -> bool:
        dp = set([0])
        numSum = 0
        maxNum = 0
        for num in nums:
            numSum += num
            maxNum = max(maxNum, num)
        goal = numSum // 2    
        if numSum % 2 == 1 or maxNum > goal:
            return False
        for num in nums:
            toAdd = set()
            for d in dp:
                if d + num == goal:
                    return True
                if d + num < goal and d + num not in dp:
                    toAdd.add(d + num)
            dp = dp | toAdd
        return False
            
            