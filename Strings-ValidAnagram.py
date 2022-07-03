class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
#sol2   return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')
        
        
