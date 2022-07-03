#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        n=len(nums)
        leftP =  [1]*n 
        rightP = [1]*n
        ans = [1]*n
       
        for i in range(1, n):               #leftProduct array
            leftP[i] = leftP[i-1] * nums[i-1]

        
        for i in reversed(range(0,n-1)):    #rightProduct array
            rightP[i] =rightP[i+1] * nums[i+1]
            
        # ans array by multiplying left and right arrays at each index
        for i in range(n):
            ans[i] = leftP[i]  *  rightP[i]
            
        return ans     
    
     
