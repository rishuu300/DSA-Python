class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def findIntersection(self, head1, head2):
        seen = set()
        
        while head2:
            seen.add(head2.data)
            head2 = head2.next
        
        dummyNode = Node(0)
        curr = dummyNode
        
        while head1:
            data = head1.data
            
            if data in seen:
                temp = Node(data)
                curr.next = temp
                curr = curr.next
            
            head1 = head1.next
        
        return dummyNode.next