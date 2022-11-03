class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        left = 0
        right = len(nums)-1
        
        while(left <= right):
            mid = left + (right-left)//2
                
            #search mid
            if (nums[mid] == target):
                return mid
                    
            #b-search left side of arr
            if (nums[left] <= nums[mid]):  
                if (target >= nums[left] and target < nums[mid]): 
                    right = mid-1
                else:
                    left = mid +1       
 
            #b-search right side of array
            else:
                if (target <= nums[right] and target > nums[mid]):
                    left = mid + 1
                else:
                    right = mid -1
        return -1
