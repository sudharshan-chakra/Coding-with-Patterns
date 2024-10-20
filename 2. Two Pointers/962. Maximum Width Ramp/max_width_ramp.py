class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0] * len(nums)
        maxr = 0

        for i in range(len(nums)-1,-1,-1):
            maxr = max(maxr,nums[i])
            max_right[i] = maxr
        
        print(max_right)

        l = 0
        max_window = 0
        for r in range(len(nums)):
            if max_right[r] < nums[l]:
                l += 1
            max_window = max(max_window,r-l)

        return max_window