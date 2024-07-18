class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        largest, smallest, largest_idx, smallest_idx = -math.inf, math.inf, 0,0
        res = 0
        last_index = len(nums)-1

        for k, num in enumerate(nums):
            if num < smallest:
                smallest_idx = k
                smallest = num
            if num >= largest:
                largest_idx = k
                largest = num

        res = (last_index - largest_idx) + smallest_idx

        return res - 1 if smallest_idx > largest_idx else res      