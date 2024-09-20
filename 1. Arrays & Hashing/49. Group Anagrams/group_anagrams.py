class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdict = defaultdict(list)

        for string in strs:
            mapping = [0] * 26

            for ch in string:
                mapping[ord(ch)-97] += 1
            
            strdict[tuple(mapping)].append(string)
        
        return [i for i in strdict.values()]