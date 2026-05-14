class Solution:
    def deleteNode(self, del_node):
        curr = del_node
        
        while curr.next.next:
            temp = curr.data
            curr.data = curr.next.data
            curr.next.data = temp
            curr = curr.next
        
        curr.data = curr.next.data
        curr.next = None