# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Given the root of a binary tree, return its maximum depth.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:        #base case
            return 0
    
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    #recursive dfs approach
    
    
