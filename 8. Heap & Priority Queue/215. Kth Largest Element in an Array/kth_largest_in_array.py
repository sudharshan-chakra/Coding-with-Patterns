import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # O(NlogK) time, O(k) space
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]

        # O(NlogN) time, O(N) space
        nums = [-i for i in nums]
        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1
        
        return nums[0]