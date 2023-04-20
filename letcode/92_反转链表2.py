class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        tail1 = None
        tail2 = None
        for i in range(1,left):
            tail1 = curr
            tail2 = curr.next
            curr = curr.next
        for j in range(right - left):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            head1 = curr
            head2 = curr.next
        tail1.next = head1
        tail2.next = head2
        return head

