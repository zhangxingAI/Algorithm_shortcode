'''
题目描述

告警抑制，是指高优先级告警抑制低优先级告警的规则。高优先级告警产生后，低优先级告警不再产生。请根据原始告警列表和告警抑制关系，给出实际产生的告警列表。

注：

不会出现循环抑制的情况。
告警不会传递，比如 A->B，B->C，这种情况下A不会直接抑制C。
但被抑制的告警仍然可以抑制其他低优先级告警。

输入描述

第一行为数字 N，表示告警抑制关系个数，O≤N≤120
接下来 N行，每行是由空格分隔的两个告警ID，例如：id1 id2，表示 id1 抑制 id2，告警ID 的格式为：
大写字母+0个或者1个数字
最后一行为告警产生列表，列表长度Q［1，100］

输出描述

真实产生的告警列表

备注

告警ID 之间以单个空格分隔

input
4
F G
C B
A G
A0 A
A B C D E

output
A C D E
'''
n = int(input())
relations = [input().split() for i in range(n)]
alertList = input().split()

def getResult():
    high = {}

    # id1抑制id2
    for id1, id2 in relations:
        if high.get(id2) is None:
            high[id2] = set()
        high[id2].add(id1)

    alertSet = set(alertList)

    ans = []

    for id2 in alertList:
        if high.get(id2) is None or alertSet.isdisjoint(high[id2]):
            ans.append(id2)

    return ' '.join(ans)
# 算法调用
print(getResult())