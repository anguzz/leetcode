class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp= [0] * (target + 1)   # 
        dp[0] = 1
        
        
        for t in range(1, target + 1): #iterate to our target value
            for n in nums:             #iterate through each of our numbers
                if n <= t:             #if that number is less then our target value
                    dp[t] += dp[t - n]      #update dp array to equal t-n
        return dp[target]
    
    
    #this problem is similar to climbing stairs problem, but instead you have n amounts of steps to reach your stair(target in this case)
    #follows the same principal, and we use a dp array to calculate the target combinations at that point using the previous indexes
    
    
    # for given example [1,2,3] t=4 with num length 3
    # our dp array will go through and start at [1,0,0,0,0] and end at [1,1,2,4,7]
    # and each dp index represents the combinations for that target
    # so for t=4, our possible combinations are 7 since we add (1+2+4)
    # and for t=5 our combinations would be 13 since we had the 3 previous numbers(2+4+7)
    # and so on

        
