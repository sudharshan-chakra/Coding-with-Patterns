class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        window = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            while nums[r] * (r-l+1) > total + k:
                total -= nums[l]
                l += 1 
            window = max(window,r-l+1)

        return window