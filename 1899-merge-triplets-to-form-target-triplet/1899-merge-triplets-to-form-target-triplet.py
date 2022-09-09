class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        Xtrip = False
        Ytrip = False
        Ztrip = False
        
        for tup in triplets:
            x,y,z = tup
            if x <= target[0] and y <= target[1] and z<=target[2]:
                if x == target[0]:
                    Xtrip = True
                if y == target[1]:
                    Ytrip = True
                if z == target[2]:
                    Ztrip = True
        
        return Xtrip and Ytrip and Ztrip
                
            