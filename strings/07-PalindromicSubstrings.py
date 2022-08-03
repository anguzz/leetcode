#Given a string s, return the number of palindromic substrings in it.

#Examples

#Input: s = "abc"
#Output: 3
#strings: "a", "b", "c".


#Input: s = "aaa"
#Output: 6
#Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i, _ in enumerate(s): #count palindromes for each index 
            result += self.countPalSubstr(s, i, i)     #for even 
            result += self.countPalSubstr(s, i, i + 1) #for odd case
        return result

    def countPalSubstr(self, s: str, left, right) -> int:
        result = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            right += 1
            left -= 1

        return result
