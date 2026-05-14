class Solution:
    def removeDuplicates(self, head):
        seen = set()
        curr = head
        prev = None
        
        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                prev = curr
                seen.add(curr.data)
            
            curr = curr.next
        
        return head