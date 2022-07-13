#Input: s = "12"
#Output: 2  (1,2) OR (12)

#input: s = "06"
#Output: 0  (06 Not valid)

class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case check
        if s is None or s[0] == '0':
            return 0
        
        dp = [1] * len(s) #dp array filled with 1
        
        for i in range(1, len(s)): 
            dp[i] =0  if int(s[i]) == 0 else dp[i - 1] # One digit check and if index is zero fill dp[i] with zero else fill it with previous i
           
            if 9 < int(s[i-1:i+1]) < 27:           # Two digit check and if after 1st index & between 10-26 and not at first index
                dp[i] += dp[i - 2 if i > 1 else 0]  #add prevPrev index
       
    # Return the length of dp
        return len(dp)
    
    #similar to climbing-steps but with extra constraints that you factor in as if statements
