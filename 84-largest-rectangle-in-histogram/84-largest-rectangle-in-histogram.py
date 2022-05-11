class Solution:
    from collections import defaultdict
    def largestRectangleArea(self, heights: List[int]) -> int:
        self.max = 0
        self.cur_max = defaultdict(int)
        def getMaxStartingLeft(height, stack, left):
            def leftShift(x, n, left):
                return x if left else n - 1 - x
            n = len(height) - 1
            for i, h in enumerate(height):
                while stack and h < stack[-1][1]:
                    idx, old_h = stack[-1]
                    new_area = (i - idx) * old_h
                    new_idx = leftShift(idx, n, left)
                    stack.pop()
                    if not left:
                        new_area -= old_h
                    self.cur_max[new_idx] += new_area
                    self.max = max(self.max, self.cur_max.get(new_idx))
                stack.append((i, h))
        heights.append(-1) 
        getMaxStartingLeft(heights, [], True)
        heights.pop()
        heights = heights[::-1]
        heights.append(-1)
        getMaxStartingLeft(heights, [], False)
        # print(self.cur_max)
        return self.max