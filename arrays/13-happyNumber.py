class Solution:
    def isHappy(self, n: int) -> bool:
        v=set()
        
        while n not in v:
            v.add(n) #add visited num to set
            n=self.sumSquares(n)
            if n==1:return True
        return False
    
    def sumSquares(self, n:int)-> int:
        ans=0
        
        while n:
            digit=n%10
            digit=digit**2
            ans+=digit
            n=n//10
        return ans
            
            #check for cycle, if a cycle occurs and we find a number we hit twice return false
            #otherwise we eventually hit 1 and return true
