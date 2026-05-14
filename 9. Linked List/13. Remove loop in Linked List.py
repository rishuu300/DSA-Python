class Solution:
    def removeLoop(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        if slow != fast:
            return
        
        if slow == head and fast == head:
            while fast.next != slow:
                fast = fast.next
            
            fast.next = None
            return
        
        slow = head
        while fast.next != slow.next:
            fast = fast.next
            slow = slow.next
        
        fast.next = None