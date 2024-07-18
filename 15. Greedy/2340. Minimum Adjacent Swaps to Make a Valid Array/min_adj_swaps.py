class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        largest, smallest, largest_idx, smallest_idx = -math.inf, math.inf, 0,0
        res = 0
        last_index = len(nums)-1

        for k, num in enumerate(nums):
            if num < smallest:
                smallest_idx = k
                smallest = num
            if num >= largest: # >= because we want the right most largest value
                largest_idx = k
                largest = num

        # the result is simply the number of places required by the right most largest index to reach the end 
        # plus the left most smallest number to reach index 0
        res = (last_index - largest_idx) + (smallest_idx - 0)

        # res-1 is needed beacuse when the small_idx is greater than the large_idx
        # there is excatly one swap when they meet (which is overlapping) so we subtract by 1.
        return res - 1 if smallest_idx > largest_idx else res     