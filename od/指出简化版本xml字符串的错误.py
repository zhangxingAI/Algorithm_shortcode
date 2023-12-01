'''
正常的xml样例如下：

<book>
<author>Cay s. Horstmann</author>
<isbn lang="CN">1234567</isbn>
<tags>
<tag>java</tag>
<tag>Network</tag>
</tags>
<pubDate/>
</book>
xml必须包含根节点，book就样例中的根节点。xml节点可以嵌套：如book和tags节点

简化版xml节点满足如下条件

1.节点的名称为单字符，如<a></a>，不会出现<ab></ab>
2.节点不带属性
3.节点不会出现<a/>
4.节点会出现带值情况如<a>Value</a>
5.xml节点包含值和包含子节点。只能二选一。
请计算给定简化版xml字符串中不合规的当前节点名称。不合规的当前节点：是指当前xml节点node1与下一个xml节点node2不匹配，则node1节点为当前节点。

题目保证输入的简化版xml，有且只有一个错误。

输入
简化版xml字符串，长度为小于1000.省略了样例中的换行符。

输出
输出给定简化版xml字符串中不合规的当前节点名称。

样例1

输入
<a><b></a>
输出
b
'''
s = input()
s = s.replace("<"," <")
s = s.replace(">","> ")
s = s.strip()
arr = s.split(" ")
for i in arr:
    if i == '':
        arr.remove(i)
def solve():
    sk = []

    def proce(s):
        return s.replace("<","").replace("/","").replace(">","")

    for a in arr:
        if a[:2] == "</":
            cnt = 0
            while sk and sk[-1] != a.replace("/", ""):
                tp = sk.pop()
                if tp[0] == '<':
                    print(proce(tp))
                    return
                cnt += 1
            if sk[-1] == a.replace("/", ""):
                sk.pop()
            if cnt > 1:
                print(proce(a))
                return
        else:
            if sk and sk[-1][0] != '<':
                #栈顶元素不为左标签
                print(proce(sk[-2]))
                return
            sk.append(a)

solve()