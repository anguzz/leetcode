class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":  #if empty zero
            return 0     
        
        left=0 
        right =0
        currMax = 0
        unique = set() #empty set to add unique chars
    
        while right < len(s):
            if s[right] not in unique: #if last char not in unique str
                unique.add(s[right])  #add to unique str
                right += 1              #increment end pointer
                currMax = max(currMax, len(unique))  #update max
            else:
                unique.remove(s[left])  #otherwise if exist remove from dict 
                left += 1    #increment start /move right 
        return currMax
