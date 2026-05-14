class Solution:
    def getKthFromLast(self, head, k):
        fast = head
        
        for i in range(k):
            if fast is None:
                return -1
            fast = fast.next
        
        slow = head
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        return slow.data