def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
      
      
      #list length (1,1,2,3,4,5) = 6 
      #set  length  (1,2,3,4,5)  = 5
      
