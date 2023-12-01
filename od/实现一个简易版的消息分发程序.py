'''
实现一个简易版的消息分发程序，客户端可以广播消息，可以订阅和取消订阅其他用户（默认订阅了自己）

每一个客户端有一个ClientID，每一条消息都有一个MsgID。请实现如下方法。

序号	方法	返回值	说明
1	Brocast(ClientID,MsgID)	返回发送的消息条数	ID为ClientID的客户端广播了一条ID为MsgID的新消息
2	GetMsg(ClientID, N)	返回最近的N条消息	获取ID为 clientID 的客户端的消息，技消息出现的先后顺序排列，如果不够N条，按实际条数输出，一条消息都没有，输出-1
3	Subscribe(ClientiD1,ClientiD2)	返回订阅状态，0表示正常订阅，1表示重复订阅，2表示自己订阅自己	ID为 clientID1的客户端1订阅ID为 clientID2的客户端2的消息，即客户端2广播的消息在客户端1订阅后，就会被其接收到
4	UnSubscribe(ClientiD1,ClientiD2)	返回取消订阅状态，0表示正常取消，其他值(1和2表示取消失败，1表示败原因是不存在此订阅关系，2表示失败原因是自己无法取消订阅自己.	ID为 clientID1的客户端1取消订阅ID为 clientID2的客户端2的消息，即客户端2广播的消息在客户端1取消订阅后，就从客户端1的消息里删除
指令按时间顺序输入，且客户端广播的消息都被系统记录不会消失，订阅生效后，能够查询到目标客户端的之前发送的消息

input
Brocast 1 5
Brocast 2 6
GetMsg 2 10
Subscribe 2 1
GetMsg 2 10
GetMsg 3 5

output
1
1
6
0
6 5
-1
'''



from collections import defaultdict

inputs = []
while True:
    user_input = input()
    if user_input == '':
        break  # 当用户输入为空行时，终止循环
    inputs.append(user_input)
print(inputs)

sends = defaultdict(list)
subs = defaultdict(list)
index = 0
for input in inputs:
    ops = input.split()
    if ops[1] not in subs:
        subs[ops[1]].append(ops[1])

    if ops[0] == 'Brocast':
        cid,msg = ops[1], ops[2]
        sends[cid].append([msg, index])
        print(len(sends[cid]))

    elif ops[0] == 'GetMsg':
        cid, N = ops[1], ops[2]
        msgs = []
        for s in subs[cid]:
            msgs += sends[s]
        if len(msgs) == 0:
            print(-1)
            continue
        msgs.sort(key=lambda x:x[1], reverse=True)

        res = []
        for i, msg in enumerate(msgs):
            mid = msg[0]
            if i == N: break
            res.append(mid)
        print(' '.join([str(c) for c in res]))


    elif ops[0] == 'Subscribe':
        cid1, cid2 = ops[1], ops[2]

        if cid1 == cid2:
            print(2)
            continue

        if cid2 in subs[cid1]:
            print(1)
            continue

        print(0)
        if cid2 not in subs[cid1]:
            subs[cid1].append(cid2)


    elif ops[0] == 'UnSubscribe':
        cid1, cid2 = ops[1], ops[2]

        if cid1 == cid2:
            print(2)
            continue
        if cid2 not in subs[cid1]:
            print(1)
            continue

        print(0)

        if cid2 in subs[cid1]:
            subs[cid1].remove(cid2)

    index+=1