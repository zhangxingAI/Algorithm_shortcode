from typing import List
from listnode import ListNode, LinkList
class Solution:
    # #迭代法
    # def mergeTwoLists(self, list1, list2):
    #     prevhead = ListNode(-1)
    #     prev = prevhead
    #     while list1 and list2:
    #         if list1.val <= list2.val:
    #             prev.next = list1
    #             list1 = list1.next
    #         else:
    #             prev.next = list2
    #             list2 = list2.next
    #         prev = prev.next
    #
    #     prev.next = list1 if list1 is not None else list2
    #
    #     return prevhead.next
    #递归法
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        elif list1.val <=list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

q = Solution()
link = LinkList()
list1 = link.initList(data = [1,1,2,2,6,7])
list2 = link.initList(data = [2,2,3,5])
ans = q.mergeTwoLists(list1 = list1, list2 = list2)
link.printlist(ans)


