class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(string):
            return string == string[::-1]
        
        l,r = 0,len(s)-1

        while l < r:
            if s[l] != s[r]:
                return is_palindrome(s[:l] + s[l+1:]) or is_palindrome(s[:r] + s[r+1:])
            l,r = l+1,r-1

        return True