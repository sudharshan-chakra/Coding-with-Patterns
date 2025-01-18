from collections import Counter, defaultdict
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count2 = defaultdict(int)
        out = []

        for word in words2:
            freq = Counter(word)
            for ch, count in freq.items():
                count2[ch] = max(count2[ch], count)
        
        for word in words1:
            freq = Counter(word)
            fit = True

            for ch, count in freq.items():
                if count2[ch] < count:
                    fit = False
                    break

            if fit:
                out.append(word)

        return word