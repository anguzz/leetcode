class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = len(nums) - 1
        nums[right] = True
        
        # from end to start
        for jump in reversed(range(right)):
            # can we jump to nearest non-zero point?
            if jump + nums[jump] >= right:
                right = jump
                
        return nums[0] >= right
    # jumping backwards to start unless you hit a zero
