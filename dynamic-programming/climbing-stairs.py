
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
     def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:   #base cases for 1 or 2 stairs
            return n
    
        prevPrev = 1    #stores i-2
        prev = 2        #stores i-1
        current = 0     #stores i
    
        for i in range(3, n+1):
            current = prevPrev + prev
            prevPrev = prev
            prev = current
        return current
