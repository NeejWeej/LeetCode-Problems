class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {}
        for idx, val in enumerate(nums):
            if val == 0:
                continue
            self.dict[idx] = val
    def val_at_idx(self, idx):
        return self.dict.get(idx, 0)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for idx, val in self.dict.items():
            ans += val * vec.val_at_idx(idx)
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)