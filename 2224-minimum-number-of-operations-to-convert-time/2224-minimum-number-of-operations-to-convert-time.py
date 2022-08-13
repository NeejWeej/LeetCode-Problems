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
        curTime = getTimeMinutes(*map(int, current.split(":")))
        corrTime = getTimeMinutes(*map(int, correct.split(":")))
        
        return getMinTimeOps(corrTime - curTime)
            
            
            
        
        
        