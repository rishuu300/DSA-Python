def removeDuplicates(head):
    curr = head
    
    while curr:
        if curr.next != None and curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head