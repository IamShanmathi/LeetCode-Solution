class Solution:

  def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
      kth = self.getKth(groupPrev, k)
      if not kth:
        break
      groupNext = kth.next

      # Reverse group
      prev, curr = groupNext, groupPrev.next
      while curr != groupNext:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

      tmp = groupPrev.next
      groupPrev.next = kth
      groupPrev = tmp

    return dummy.next

  def getKth(self, curr, k):
    while curr and k > 0:
      curr = curr.next
      k -= 1
    return curr
        