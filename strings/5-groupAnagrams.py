from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)  #dic list to count anagrams
        
        for word in strs:            
            key = [0]*26 
            for char in word:       
                key[ord(char) - ord('a')] += 1 
            lookup[tuple(key)].append(word)
        return lookup.values()
                
#iterate through all our words
#iterate through each letter of are words and get count
#get count pattern in that current word
#use that count pattern to see what other words may have that

                                
