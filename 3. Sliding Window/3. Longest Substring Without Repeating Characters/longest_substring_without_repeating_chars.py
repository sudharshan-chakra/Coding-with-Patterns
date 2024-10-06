class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        l,r = 0,0
        max_window = 0
        seen = set()

        while r < length:
            while l <= r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            while r < length and s[r] not in seen:
                seen.add(s[r])
                r += 1
                
            max_window = max(max_window,len(seen))

        return max_window
