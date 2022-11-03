#Given an integer array nums, 
#return all the triplets [nums[i], nums[j], nums[k]]= 0 
#and such that i != j, i != k, and j != k


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                                 # We sort nums first to more easily find duplicate numbers
        ans = []                                    # We will store all the valid triplets in here
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:    # if left neighbor of curr matches curr skip
                continue  
                
                
             
            left = i + 1                            #2sum with left and right ptrs   
            right = len(nums) - 1
            
            while left < right:    
                Sum = nums[i] + nums[left] + nums[right]
                
                if Sum < 0:      #too small, increase sum
                    left += 1       
                elif Sum > 0:
                    right -= 1    #too big, decrease sum
                elif Sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])   
                    left += 1     
                    while nums[left]==nums[left-1] and left<right:  #shift left pointer while not dupe and greater right 
                        left+=1    
        return ans
