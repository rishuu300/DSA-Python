class Solution:
    def isCircular(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if fast == slow:
                return True
            
            slow = slow.next
            fast = fast.next.next
        
        return False