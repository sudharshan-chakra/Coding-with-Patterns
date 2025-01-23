'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr, abbr_ptr = 0,0

        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr] == '0':
                    return False

                count = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    count = (10 * count) + int(abbr[abbr_ptr]) 
                    abbr_ptr += 1
                word_ptr += count
            
            else:
                
                if word_ptr >= len(word) or abbr[abbr_ptr] != word[word_ptr]:
                    return False
                
                # increment only when the abbr[abbr_ptr] is a char
                abbr_ptr += 1
                word_ptr += 1
        
        return abbr_ptr == len(abbr) and word_ptr == len(word)
