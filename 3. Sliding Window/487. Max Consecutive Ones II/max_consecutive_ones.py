class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_ones = max_ones = 0
        window_zeros = 0
        l = r = 0
        
        while r < len(nums):
            if nums[r] == 0:
                window_zeros += 1
                
            while window_zeros > 1:
                if nums[l] == 0: 
                    window_zeros -= 1
                l += 1

            window = r-l+1
            max_ones = max(max_ones, window)
            r += 1
            
        return max_ones