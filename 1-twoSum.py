 #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
           
