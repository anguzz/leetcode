class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #two pointer solution
        ans=0
        left=0
        right= len(height)-1
        
        while (left< right):                          
            currWidth = right-left
            
            if height[left] <= height[right]:         
                tempMax = height[left] * (currWidth) 
                left += 1
            
            elif height[left] >= height[right]:
                tempMax =height[right] * (currWidth)
                right -= 1
            
            if tempMax > ans: ans = tempMax
        return ans
