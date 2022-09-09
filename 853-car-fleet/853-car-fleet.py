class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if one ahead arrives later or at same time, they intersect
        # if fleets join, can "pretend" theyre one to make later 
        # calculations easier
        
        #if fleet intersects, then poistion is min, and the slope is
        # (start - end)/ (endTime)
        # endTime is still the same as previous fleet
        
        def intersect(x, y):
            # if y gets there later they hit
            # x[0] + x[1]*t = target
            # t = (target - x[1]) /x[0]
            xTime = (target - x[0]) / x[1]
            yTime = (target - y[0]) / y[1]
            if xTime <= yTime:
                return True, yTime
            return False, xTime
        
        posSort = sorted(zip(position, speed), key = lambda x: target - x[0])
        stack = []
        
        for p, s in posSort:
            if stack:
                intersec, time = intersect((p,s), stack[-1])
                if not intersec:
                    stack.append([p, s])
                    continue
                stack[-1] = [p, (target - p)/time]
            else:
                stack.append([p, s])
        # print(stack, p,s)
        return len(stack)