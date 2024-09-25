class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        out = []

        for k,num in enumerate(nums):
            num = abs(num)
            if nums[num-1] < 0:
                out.append(num)
            nums[num-1] *= -1

        return out 
