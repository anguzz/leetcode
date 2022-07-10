#Input: nums = [10,9,2,5,3,7,101,18]
#Output: 4
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        LIS = [1] * n #cache of length of list all set to 1
        
        for i in range(n-1, -1, -1): #iterate backwards
            for j in range(i+1, n):  #iterate forwards
                if nums[i]<nums[j]: #if increasing
                    LIS[i]= max(LIS[i],LIS[j]+1) #compare the maxes of curr and prev LIS
        return max(LIS)
