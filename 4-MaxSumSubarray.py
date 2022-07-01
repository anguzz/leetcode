#kandane's algo
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]    
        for i in range(1,len(nums)):
            currSum= max(nums[i]+currSum, nums[i]) #compare all elems to that point and curr element and get max between two
            maxSum = max(maxSum, currSum) #check if that subarray currSum is greater then saved maxSum and reassign 
        return maxSum
