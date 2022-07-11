from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)  #dic list to count anagrams
        
        for word in strs:            
            frequencyList = [0]*26 
            for char in word:       
                frequencyList[ord(char) - ord('a')] += 1 
            d[tuple(frequencyList)].append(word)
        return d.values()
                
#iterate through all our words
#iterate through each letter of are words and get count
#get count pattern in that current word
#use that count pattern to see what other words may have that

                                
