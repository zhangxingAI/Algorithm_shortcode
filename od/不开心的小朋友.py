'''
游乐场里增加了一批摇摇车，非常受小朋友欢迎，但是每辆摇摇车同时只能有一个小朋友使用，如果没有空余的摇摇车需要排队等候，或者直接离开，最后没有玩上的小朋友会非常不开心。

请根据今天小朋友的来去情况，统计不开心的小朋友数量

1. 摇摇车数量为N，范围是：1<=N < 10；

2. 每个小朋友都对应一个编码，编码是不重复的Q数字，今天小朋友的来去情况，可以使用编码表示为：112323。 （若小朋友离去之前有空闲的摇摇车，则代表玩耍后离开；不考虑小朋友多次玩的情况）。小朋友数量≤100

3.题目保证所有输入数据无异常且范围满足上述说明

输入描述

第一行：摇摇车数量
第二行：小朋友来去情况

输出描述

返回不开心的小朋友数量

input
1
1 2 1 2
output
0

说明
第一行，1个摇摇车
第二行，1号来 2号来（排队）1号走 2号走（1号走后摇摇车已有空闲，所以玩后离开）

input
1
1 2 2 3 1 3
output
1

说明
第一行，1个摇摇车
第二行，1号来2号来（排队）2号走（不开心离开）3号来（排队）1号走3号走（1号走后摇摇车已有空闲，所以玩后离）
'''

def getresults():
    capacity = int(input())
    people = input().split(' ')
    ans = []
    setpeople = set(people)
    play = set()
    for p in people:
        if capacity > 0 and p not in play:
            play.add(p)
            capacity -= 1
        elif p in play:
            capacity += 1
    for i in setpeople:
        if i not in play:
            ans.append(i)
    return len(ans)

print(getresults())




