from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l,r = 0,0
        length = len(s)
        longest = 0
        maxf = 0

        while r < length:
            counter[s[r]] += 1
            maxf = max(maxf, counter[s[r]])  
            while (r-l+1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest,r-l+1)
            r += 1

        return longest