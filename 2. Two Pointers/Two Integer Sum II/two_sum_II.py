class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        out = []
        length = len(numbers)

        def search(l,r,tar):
            while l <= r:
                m = (l+r)//2
                if numbers[m] > tar:
                    r = m-1
                elif numbers[m] < tar:
                    l = m+1
                else:
                    return m
            return -1

        for k,num in enumerate(numbers):
            tar = target - num
            l = k+1
            idx = search(l,length-1,tar)

            if idx >= 0:
                return [k+1,idx+1]