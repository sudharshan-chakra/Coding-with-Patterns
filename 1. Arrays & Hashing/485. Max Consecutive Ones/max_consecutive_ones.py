class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_ones = max_ones = 0
        length = len(nums)

        for r, num in enumerate(nums):
            if num == 0:
                window_ones = 0
            else:
                window_ones += 1

            max_ones = max(max_ones, window_ones)

        return max_ones