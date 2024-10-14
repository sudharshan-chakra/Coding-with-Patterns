class Solution:
    def minLength(self, s: str) -> int:
        length = len(s)

        while True:
            isPresent = False

            for i in range(1,length):
                if s[i-1:i+1] in ["AB","CD"]:
                    isPresent = True
                    s = s[:i-1] + s[i+1:]
                    break

            if not isPresent:
                return len(s)