class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        
        hand.sort()
        n = len(hand)
        # groups = collections.defaultdict(list)
        groups = collections.defaultdict(dict)
        for h in hand:
            if h - 1 in groups:
                count = next(iter(groups.get(h-1)))
                val = groups[h-1].pop(count)
                if val > 1:
                    groups[h-1][count] = val - 1
                
                elif not groups[h - 1]:
                    del groups[h - 1]
                
                if count != groupSize - 1:
                    groups[h][count + 1] = groups[h].get(count + 1, 0) + 1
            else:
                groups[h][1] = groups[h].get(1, 0) + 1
        return len(groups) == 0
                