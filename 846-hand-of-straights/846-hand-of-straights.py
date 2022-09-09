class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        
        hand.sort()
        n = len(hand)
        groups = collections.defaultdict(list)
        for h in hand:
            if h - 1 in groups:
                prevGroup = groups[h - 1].pop()
                if len(groups[h-1]) == 0:
                    del groups[h-1]
                
                if len(prevGroup) != groupSize - 1:
                    prevGroup.append(h)
                    groups[h].append(prevGroup)
            else:
                groups[h].append([h])
        return len(groups) == 0
        
        # end = -1
        # Ihand = iter(hand)
        # next(Ihand)
        # for i,h in enumerate(Ihand, 1):
        #     if h > hand[i - 1]:
        #         if i - end + 1 == groupSize:
        #             end = i
        #     elif i - end + 1 > groupSize:
        #         return False
        # return end == n - 1
                