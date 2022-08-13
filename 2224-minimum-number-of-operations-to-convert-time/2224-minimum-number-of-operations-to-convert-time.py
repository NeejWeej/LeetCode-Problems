class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def getMinTimeOps(val):
            ans = 0
            for time in times:
                ans += val // time
                val %= time
            return ans
        
        def getTimeMinutes(hours, minutes):
            return 60*hours + minutes
        
        times = [60, 15, 5, 1]
        curHr, curMin = map(int, current.split(":"))
        corrHr, corrMin = map(int, correct.split(":"))
        
        curTime = getTimeMinutes(curHr, curMin)
        corrTime = getTimeMinutes(corrHr, corrMin)
        return getMinTimeOps(corrTime - curTime)
            
            
            
        
        
        