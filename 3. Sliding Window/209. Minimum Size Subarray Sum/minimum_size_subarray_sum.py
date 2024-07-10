class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        window_sum = 0
        shortest = float('inf')

        while r < len(nums):
            window_sum += nums[r]
            r += 1
    
            while r < len(nums) and window_sum < target:
                window_sum += nums[r]
                r += 1

            while window_sum >= target:
                shortest = min(shortest, r-l)
                window_sum -= nums[l]
                l += 1

        return shortest if shortest != float('inf') else 0