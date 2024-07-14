class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest = float('inf')
        l = 0
        window_sum = 0

        for r, val in enumerate(nums):
            window_sum += val
            while window_sum >= target:
                smallest = min(smallest, r-l+1)
                window_sum -= nums[l]
                l += 1

        return 0 if smallest == float('inf') else smallest