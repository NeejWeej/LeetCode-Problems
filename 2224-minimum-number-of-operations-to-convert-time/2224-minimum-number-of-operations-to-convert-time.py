class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def getMinTimeOps(val):
            ans = 0
            for time in times:
                ans += val // time
                val %= time
            return ans
        
        times = [15, 5, 1]
        curHr, curMin = map(int, current.split(":"))
        corrHr, corrMin = map(int, correct.split(":"))
        
        if curMin <= corrMin:
            res = (corrHr - curHr) % 24
            diff = corrMin - curMin
        else:
            # in this case, since curr <= corr, know corrHr > curHr
            res = (corrHr - curHr - 1) % 24
            diff = (60 - curMin) + corrMin
        res += getMinTimeOps(diff)
        return res
            
            
            
        
        
        