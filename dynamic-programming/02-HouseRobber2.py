class Solution:       
     def rob2(self, nums: List[int]) -> int:  
        #create arr
        rob = [0] * (len(nums) + 1)  
        # Base case: 0 rooms and 1 room
        rob[0] = 0
        rob[1] = nums[0]     
        # Solving sub questions and store the sub solutions: more than 1 rooms
        for i in range(2, len(nums) + 1):
            # For any given number at index n: compare dp[n-2] + number and dp[n-1]
            rob[i] = max(rob[i-2] + nums[i-1], rob[i-1])
        # Return the larget amount of money stolen from the results
        return rob[len(nums)]
     
     
     #alternative solution
     def rob(self, nums: List[int]) -> int: #very similar to climb steps, but get the max here
        prev= prevPrev=0
        
        for n in nums:
            temp=max(n+prev, prevPrev)
            prev= prevPrev
            prevPrev = temp
        return temp
