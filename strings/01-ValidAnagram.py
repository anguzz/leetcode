class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
#2nd method  return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')
        
#  Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#Input: s = "anagram", t = "nagaram" Output: true
