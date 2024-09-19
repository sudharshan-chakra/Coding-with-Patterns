class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numslist = collections.defaultdict(int)

        for k,num in enumerate(nums):
            numslist[num] = k 

        for k,num in enumerate(nums):
            search = target - num
            if search in numslist and k != numslist[search]:
                return [k,numslist[search]]