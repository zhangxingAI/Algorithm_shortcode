'''
有一个快递代收点，代收点会陆续收到一批批快递，代收点会将这些快递集中暂时保管。
每个快递都有手机号标识，快递的最终收件人会以手机号为凭证到该快递点拿走快递。
代收点对超过3天未取走的快递会收取保管费，每超出1天收取1块钱。
请创建合适的数据结构，管理代收点批量收取的快递，实现收件人取走自己所有快递的操作，并计算出总共需要支付的超期保管费。

输入

第一行为数字N，代表接下来会有N个批次的快递到达代收点。接下来的N行是快递达到的详细信息，每一行代表某一天达到代收点的快递。
第一个字符串为日期，后面是当前批次的快递手机号，每一批的快递件数为M。
最后一行是到代收点取件顾客的手机号和取件日期，且一次仅有一个顾客取件，取件日期和快递到达的日期相同时当作可取件处理。
0< N<1000,0<M<100,所有手机号均为11位数字。
输入中所有出现的日期均属于2023年。

输出
收件人在给定的时间可取走的快递件数以及需要支付的超期保管费数目。

input
2
2023-01-01 15012345678  13812345678 13812345678 13812345678 13812345678
2023-01-02 15112345678 13912345678 13812345678 13712345678 19812345678
2023-01-05 13812345678

output
5 4
'''
from collections import defaultdict
from datetime import datetime
N = int(input())
date_format = "%Y-%m-%d"
cnt = defaultdict(list)

for _ in range(N):
    tmp = input().split()
    date = datetime.strptime(tmp[0], date_format)
    for i in range(1, len(tmp)):
        cnt[tmp[i]].append(date)

date, phone = input().split()
date = datetime.strptime(date, date_format)

num = 0
money = 0

for dv_date in cnt[phone]:
    if dv_date <= date:
        num += 1
        diff = (date-dv_date).days
        if diff > 3:
            money += diff-3

print(num, money)