class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        running_sum = 0
        sums = [0]
        for idx, num in enumerate(nums):
            running_sum += num
            sums.append(running_sum)
        
        def merge(lo, h):
            if lo <= h <= lo + 1:
                return 0
            mid = lo + (h - lo) // 2
            count = merge(lo, mid) + merge(mid, h)
            start = end = mid
            for left in sums[lo:mid]:
                while start < h and sums[start] - left < lower:
                    start += 1
                end = max(start, end)
                while end < h and sums[end] - left <= upper:
                    end += 1
                count += end - start
            
            lsi = lo
            rsi = mid
            new = []
            while lsi < mid or rsi < h:
                if lsi == mid:
                    new += sums[rsi: h]
                    break
                if rsi == h:
                    new += sums[lsi: mid]
                    break
                if sums[lsi] <= sums[rsi]:
                    new.append(sums[lsi])
                    lsi += 1
                else:
                    new.append(sums[rsi])
                    rsi += 1
            sums[lo: h] = new
            # sums[lo:h] = sorted(sums[lo:h])
            return count
        return merge(0, len(sums))
        