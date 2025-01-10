class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort 
        nums.sort()
        return nums[len(nums)//2]

        # candidate and count
        candidate, count = 0,0

        for num in nums:
            if count == 0:
                candidate = num
            
            if num != candidate:
                count -= 1
            else:
                count += 1
        
        return candidate