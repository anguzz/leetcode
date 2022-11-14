class BSTIterator:
#Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
    def __init__(self, root: Optional[TreeNode]):
        
        self.l = []
        q = [root]
        while q:
            node = q.pop(0)
            self.l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        self.l = sorted(self.l)
        
    def next(self) -> int:
        n = self.l.pop(0)
        return n

    def hasNext(self) -> bool:
        return len(self.l) > 0
