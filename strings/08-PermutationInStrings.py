#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#s1 = "ab"
#s2 = "eidbaooo"
#true, s2 contains ba = ab

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = Counter(s1)
        hashmap2 = {}
        l=0         #left ptr
        r=len(s1)   #right ptr

        while r < len(s2) + 1:
            if hashmap1 == Counter(s2[l:r]):
                return True
            l += 1
            r += 1
        return False
