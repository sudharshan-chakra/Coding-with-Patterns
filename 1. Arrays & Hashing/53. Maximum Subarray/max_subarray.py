class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        cur_sum = 0
        max_sum = nums[0]

        if len(nums) == 1: return nums[0]

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        
        return max_sum