from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key = lambda x: x[1])
        dest = defaultdict(dict)
        for from_, to_ in tickets:
            dest[from_][to_] = 1 + dest[from_].get(to_, 0)
        
        self.res = None
        cur = 'JFK'
        
        def recSearch(flights, cur, res):
            res.append(cur)
            if len(flights) == 0 and not self.res:
                self.res = res[:]
            
            if self.res:
                return
            
            curFlights = list(flights.get(cur, {}).keys())
            
            for to_ in curFlights:
                actualFlights = flights.get(cur, {})
                actualFlights[to_] -= 1
                if actualFlights[to_] == 0:
                    actualFlights.pop(to_)
                if len(actualFlights) == 0:
                    flights.pop(cur)
                
                recSearch(flights, to_, res)
                flights[cur][to_] = 1 + flights[cur].get(to_, 0)
            
            res.pop()
            
            
        recSearch(dest, cur, [])
        return self.res

        