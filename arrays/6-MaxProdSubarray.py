
#Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = 1 
        mn = 1
        ans = max(nums)
        
        for n in nums:
            mx = max(n, mx*n, mn*n)
            mn = min(n, mx*n, mn*n)
            ans= max(mx, mn, ans)
        return ans
            
   #keep track of curr min and max due to the sign of the numbers
   #we track the min value incase of negative value
 
