#find the longest palindromic substring 

#Input: s = "babad"
#Output: "bab"
#Output: "aba" also valid

#Input: s = "cbbd"
#Output: "bb" 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #go to the middle and expand outwards
        #use double pointers 
        left = right = middle = 0 
        longestString = ""
        
        #for odd len string 
        while (middle < len(s)):
            #set value at left and right the same 
            left = right = middle
             #conditions to move left and right while equal 
            while(left >= 0 and right < len(s) and s[left] == s[right]): 
                #store the string 
                currentString = s[left: right + 1]
                #expand outwards by moving left and right pointers
                left = left - 1
                right = right + 1
            
            if len(currentString) >= len(longestString): #update longeststring to temp/current string
                longestString = currentString
                
            #traverse
            middle = middle + 1
        
        #for even len string (most stays the same except we start the right at offset of 1 )  
        left = right = middle = 0
        while (middle < len(s)):
            left = right = middle
            right = right + 1
            
            while(left >= 0 and right < len(s) and s[left] == s[right]): 
                currentString = s[left: right + 1]
                left = left - 1
                right = right + 1
    
            if len(currentString) >= len(longestString):
                longestString = currentString
            
            middle = middle + 1
            
        return longestString
