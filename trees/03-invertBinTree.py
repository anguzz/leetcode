# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  #base case if root is null
            return None 
        
        
        #swap children 
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left) #recurvise calls 
        self.invertTree(root.right)
        
        return root
        
