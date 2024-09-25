class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        cur = best = 0

        for num in nums:
            if num-1 not in numset:
                cur = 1
                this = num+1
                while this in numset:
                    cur += 1
                    this += 1
                best = max(best, cur)
        
        return best