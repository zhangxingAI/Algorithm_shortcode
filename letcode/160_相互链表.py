# 迭代解法
class Solution:
#hash表方法
    # def getIntersectionNode(self, headA, headB):
    #     s = set()
    #     p, q = headA, headB
    #     while p:
    #         s.add(p)
    #         p = p.next
    #     while q:
    #         if q is in s:
    #             return q
    #         q = q.next
    #     return None

#双指针方法
    def getIntersectionNode(self, headA, headB):
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return q




