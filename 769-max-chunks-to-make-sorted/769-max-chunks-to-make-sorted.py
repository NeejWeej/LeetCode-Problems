class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        spotsSorted = {}
        arrSorted = sorted(arr)
        for idx, num in enumerate(arrSorted):
            spotsSorted[num] = idx
        count = 0
        maxL = 0
        for idx, num in enumerate(arr):
            spot = spotsSorted.get(num)
            if spot == n - 1:
                return count + 1
            maxL = max(maxL, spot)
            if maxL == idx:
                count += 1
        return count
            
        