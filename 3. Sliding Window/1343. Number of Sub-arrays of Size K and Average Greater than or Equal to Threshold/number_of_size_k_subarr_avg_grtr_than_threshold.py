class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        length = len(arr)
        l = 0
        avg = 0
        count = 0

        for r in range(length):
            if r-l+1 > k:
                avg = avg - arr[l]/k
                l += 1
            avg = avg + arr[r]/k
            if r-l+1 == k and avg >= threshold:
                count += 1
        
        return count