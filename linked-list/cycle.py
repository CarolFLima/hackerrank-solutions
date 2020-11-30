def has_cycle(head):
    if head is None:
        return False
    
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None: 
            return False
        
        slow = slow.next
        fast = fast.next.next
    
    return True
