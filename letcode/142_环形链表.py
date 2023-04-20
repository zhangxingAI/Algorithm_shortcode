from listnode import ListNode, LinkList
class Solution:
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if fast is None or fast.next is None:
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

