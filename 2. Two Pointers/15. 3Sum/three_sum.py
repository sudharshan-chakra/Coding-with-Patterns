class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        out = []

        for i,num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1,length-1
            while l < r:
                target = num + nums[l] + nums[r]

                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    out.append([num,nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l > 0 and l < length and nums[l] == nums[l-1]:
                        l += 1
        
        return out
