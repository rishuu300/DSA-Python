class Solution:
    def pairWiseSwap(self, head):
        curr = head.next.next
        prev = head
        head = head.next
        head.next = prev
        
        while curr and curr.next:
            prev.next = curr.next
            prev = curr
            next = curr.next.next
            curr = curr.next
            curr.next = prev
            curr = next
        
        prev.next = curr
        
        return head