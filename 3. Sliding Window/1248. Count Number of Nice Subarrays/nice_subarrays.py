class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l,m = 0,0
        res = 0
        length = len(nums)
        is_odd = lambda x: x % 2
        odd_count = 0

        for r,num in enumerate(nums):
            if is_odd(num):
                odd_count += 1

            while odd_count > k:
                if is_odd(nums[l]):
                    odd_count -= 1
                l += 1
                m = l

            if odd_count == k:
                while not is_odd(nums[m]):
                    m += 1
                res += (m-l+1)   

        return res
