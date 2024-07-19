class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        for_set = set(forbidden)
        max_valid = 0
        l, length_word = 0, len(word)
        max_for = max(len(x) for x in forbidden) if forbidden else 0

        for r in range(length_word):
            for length in range(1, max_for+1): 
                if r-length+1 >= l: # Check if the left bound is greater than l, i.e window is valid 
                    if word[r-length+1:r+1] in for_set:
                        l = r-length+1 + 1
                        break

            max_valid = max(max_valid, r-l+1)

        return max_valid 