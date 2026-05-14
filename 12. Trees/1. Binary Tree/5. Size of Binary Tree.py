class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getSize(self, node):
        if node is None:
            return 0
        return 1 + self.getSize(node.left) + self.getSize(node.right)