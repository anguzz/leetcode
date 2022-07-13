class Solution(object):
	def rob(self, nums: List[int]):
		n = len(nums)  
        
		if n == 0: #base cases for 0, 1, 2 houses
			return 0
		if n == 1:
			return nums[0]
		if n == 2:
			return max(nums[1], nums[0])
        
        
       # same as house robber 1,
       # since list is circular now we can only choose to rob the first and leave last, or rob last and leave first since they're adjacent
       #because of this we loop through scenarios for both and choose max between both scenarios
	   
     
       
		robFirst, leaveLast = nums[1], nums[0]  # rob1 first house, leave last
		for i in range(2, n-1):                  #loop until previous to last house
			robFirst, leaveLast = leaveLast + nums[i], max(robFirst, leaveLast)
    
		  
		robLast, leaveFirst = nums[2], nums[1]   #rob2 last house, leave first
		for i in range(3, n):                    #include very last house 
			robLast, leaveFirst = leaveFirst + nums[i], max(robLast, leaveFirst)
    
	   
		return max(robFirst, leaveLast, robLast, leaveFirst)
        
