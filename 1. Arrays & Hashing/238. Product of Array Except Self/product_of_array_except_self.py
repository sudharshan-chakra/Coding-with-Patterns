class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right = [1] * length, [1] * length

        for k in range(1,length):
            left[k] = nums[k-1] * left[k-1] 

        for k in range(length-2,-1,-1):
            right[k] = nums[k+1] * right[k+1]
        
        return [i*j for i,j in zip(left,right)]