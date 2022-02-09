class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_so_far = float('-inf')
        can_see = []
        n = len(heights)
        idx = n - 1
        for b in reversed(heights):
            if b > max_so_far:
                can_see.append(idx)
                max_so_far = b
            idx -= 1
        can_see.reverse()
        return can_see