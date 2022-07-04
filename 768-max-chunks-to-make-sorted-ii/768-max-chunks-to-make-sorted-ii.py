class Solution:
    from collections import defaultdict, deque
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        spotsSorted = defaultdict(deque)
        arrSorted = sorted(arr)
        for idx, num in enumerate(arrSorted):
            spotsSorted[num].append(idx)
        count = 0
        maxL = 0
        for idx, num in enumerate(arr):
            spots = spotsSorted.get(num)
            spot = spots.popleft()
            if spot == n - 1:
                return count + 1
            maxL = max(maxL, spot)
            if maxL == idx:
                count += 1
        return count