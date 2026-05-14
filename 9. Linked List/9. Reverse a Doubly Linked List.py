class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        
        curr = head
        prev = None
        
        while curr:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev
        
        head = prev.prev
        
        return head