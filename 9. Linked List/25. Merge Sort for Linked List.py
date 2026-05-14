class Solution:
    def findMid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, head1, head2):
        if head1.data > head2.data:
            temp = head1
            head1 = head2
            head2 = temp
        
        res = head1
        
        while head1 != None and head2 != None:
            curr = None
            
            while head1 != None and head1.data <= head2.data:
                curr = head1
                head1 = head1.next
            
            curr.next = head2
            
            temp = head1
            head1 = head2
            head2 = temp
        
        return res
    
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        
        mid = self.findMid(head)
        left, right = head, mid.next
        mid.next = None
        
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        
        return self.merge(left, right)