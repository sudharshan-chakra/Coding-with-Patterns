class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l = 0
        length = len(s)
        maxf = 0
        longest = 0

        for r in range(length):
            counter[s[r]] += 1
            maxf = max(maxf, counter[s[r]])

            if (r-l+1) - maxf <= k:
                longest = max(longest,r-l+1)

            while (r-l+1) - maxf > k:
                counter[s[l]] -= 1
                l += 1

        return longest