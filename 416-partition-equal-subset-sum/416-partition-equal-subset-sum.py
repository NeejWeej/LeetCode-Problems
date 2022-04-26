class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # speeds up the program
        nums.sort(reverse=True)
        # if sum of elements cant be divided equally
        if sum(nums) % 2: return False
        target = sum(nums) // 2
        possible_sums = set([0])

        for el in nums:
            # using a temporary holder to not update possible_sums during cycle run
            next_sums = set()
            for s in possible_sums:
                # if target sum is found, we may assume the other "half" is contained in 
                # the remaining elemnts of nums
                if s + el == target:
                    return True
                next_sums.add(s+el)
            possible_sums.update(next_sums)
        return False
                
            