from listnode import ListNode, LinkList
class Solution:
    def partition(self, head, x):
        prevhead1 = ListNode(-1)
        prevhead2 = ListNode(-2)
        prev1 = prevhead1
        prev2 = prevhead2
        while head:
            if head.val < x:
                prev1.next = head
                prev1 = prev1.next
            else:
                prev2.next = head
                prev2 = prev2.next
            head = head.next
        prev2.next = None #防止出现闭环
        # print(prev2.next.val)
        prev1.next = prevhead2.next
        return prevhead1.next

q = Solution()
link = LinkList()
list = link.initList(data = [1,4,3,2,5,2])
ans = q.partition(head = list, x =3)
link.printlist(ans)
