"""
    给你单链表的头节点head ，请你反转链表，并返回反转后的链表。
    示例 1：
    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]
    示例 2：
    输入：head = [1,2]
    输出：[2,1]
    示例 3：
    输入：head = []
    输出：[]
"""
from listnode import ListNode, LinkList
# # 迭代解法
# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         prev, curr = None, head
#         while curr is not None:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         return prev

# 递归解法
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p

q = Solution()
link = LinkList()
b = link.initList(data = [1,1,2,3,4])
link.printlist(q.reverseList(b))