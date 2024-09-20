class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        counter = defaultdict(int)
        order = [[] for _ in range(len(nums)+1)] 

        for num in nums:
            counter[num] += 1
        
        for num,freq in counter.items():
            order[freq].append(num)
        
        length = len(order)
        for i in range(length-1,-1,-1):
            for num in order[i]:
                if k == 0:
                    break
                out.append(num) 
                k -= 1
            
        return out
