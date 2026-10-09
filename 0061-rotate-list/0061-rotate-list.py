from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Calculate length and find tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        tail.next = head  # Form circular list
        k %= length
        steps_to_new_head = length - k
        
        new_tail = tail
        while steps_to_new_head > 0:
            new_tail = new_tail.next
            steps_to_new_head -= 1
            
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
        