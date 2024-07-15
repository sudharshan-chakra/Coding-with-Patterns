class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        robs = {0:nums[0], 1:max(nums[0],nums[1])}
        
        def robHouse(idx):
            if idx < 0: return 0
            if idx in robs:
                return robs[idx]

            robs[idx] = max(nums[idx] + robHouse(idx-2), robHouse(idx-1))
            return robs[idx]
        
        return robHouse(len(nums)-1)