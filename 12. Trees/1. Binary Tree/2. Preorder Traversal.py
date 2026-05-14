class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def traversal(self, root, result):
        if root is None:
            return
        
        result.append(root.data)
        self.traversal(root.left, result)
        self.traversal(root.right, result)
    
    def preOrder(self, root):
        result = []
        self.traversal(root, result)
        
        return result