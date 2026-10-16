class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head
            
        dummy = ListNode(0, head)
        prev = dummy
        
        # 1. Reach the node just before 'left'
        for _ in range(left - 1):
            prev = prev.next
            
        curr = prev.next
        
        # 2. Reverse the sublist from left to right
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next
        