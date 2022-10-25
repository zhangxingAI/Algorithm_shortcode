class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList:
    def __init__(self):
        self.__head = None

    def initList(self,data):
        self.__head = ListNode(data[0])
        r = self.__head
        p = self.__head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self,head):
        ls = list()
        if head == None:
            return
        node = head
        while node != None:
            ls.append(node.val)
            # print(node.val, end = '')
            node = node.next
        print(ls)