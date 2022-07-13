class Solution:
    def rob(self, nums: List[int]) -> int:
        prev= prevPrev=0
        
        for n in nums:
            temp=max(n+prev, prevPrev)
            prev= prevPrev
            prevPrev = temp
        return temp
