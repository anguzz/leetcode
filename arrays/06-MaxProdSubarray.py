#Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = maxP = minP = nums[0]
        for n in nums[1:]:  
            maxP, minP = max(n, maxP*n, minP*n), min(n, maxP*n, minP*n) #imporant this happens in single line so maxP/minP are not yet affected in max/min function
            res = max(res, maxP)
        return res
        
        
        #longer readable solution
        ''' 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0: #base case
            return 0
        
        res = maxP = minP = nums[0]
        
        for i in range(1, len(nums)):
            curr=nums[i]
            tempMax = max(curr, maxP*curr, minP*curr)
            minP    = min(curr, maxP*curr, minP*curr) 
            maxP    = tempMax
            res     = max(res, maxP)
            
        return res
        '''
    
  
    

   
   
  
