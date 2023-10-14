'''
让我们来模拟一个工作队列的运作，有一个任务提交者和若干任务执行者，执行者从1开始编号。
•提交者会在给定的时刻向工作队列提交任务，任务有执行所需的时间，执行者取出任务的时刻加上执行时间即为任务完成的时刻。
•执行者完成任务变为空闲的时刻会从工作队列中取最老的任务执行，若这一时刻有多个空闲的执行者，其中优先级最高的会执行这个任务。编号小的执行者优先级高。
初始状态下所有执行者都空闲。
•工作队列有最大长度限制，当工作队列满而有新的任务需要加入队列时，队列中最老的任务会被丢弃。
•特别的，在工作队列满的情况下，当执行者变为空闲的时刻和新的任务提交的时刻相同时，队列中最老的任务被取出执行，新的任务加入队列。

输入描述

输入为两行。第一行为 2N 个正整数，代表提交者提交的N个任务的时刻和执行时间。第一个数字是第一个任务的提交时刻，第二个数字是第一个任务的执行时间，
以此类推。用例保证提交时刻不会重复，任务按提交时刻升序排列Q。
第二行为两个数字，分别为工作队列的最大长度和执行者的数量。两行的数字都由空格分隔。N不超过 20，数字为不超过 1000 的正整数。

输出描述

输出两个数字，分别为最后一个任务执行完成的时刻和被丢弃的任务的数量，数字由空格分隔。

示例一
input
1 3 2 2 3 3
3 2
output
1 0

说明
有两个执行者，执行者1号在时刻1取出了第1个任务，该任务需时为3，故1号会在时刻4完成任务；执行者2号在时刻2取出了第2个任务，该任务需时为2，
故2号也会在时刻4完成任务；第3个任务在时刻3提交，但此时没有空闲的执行者，故缓存在队列中，直到时刻4两个执行者都变为空闲，此时执行者1号会取出这个任务，
该任务需时为3， 故会在时刻7完成任务。期间没有任务被丢弃。
'''
from queue import Queue
data = list(map(int, input().split(' ')))
jobs = [[0 for i in range(2)] for j in range(int(len(data)/2))]
job_q = []
for i in range(0, len(data), 2):
    jobs[int(i/2)][0] = data[i]
    jobs[int(i/2)][1] = data[i+1]
l, n = map(int, input().split(' '))

def getresult():

    queue = []
    ans = []
    drop = 0
    x = 0
    i = 1
    total_time =0
    capacity = [0 for i in range(n)]

    while x < len(jobs) or len(queue)>0:

        if len(queue) > 0:
            for j in range(n):
                if capacity[j] == 0 and len(queue) > 0:
                    capacity[j] = queue[0]
                    queue.pop(0)

        for j in range(n):
            if capacity[j] != 0:
                capacity[j] -= 1

        if x < len(jobs) and i == jobs[x][0]:
            if l > len(queue):
                queue.append(jobs[x][1])
            elif len(queue) == l and min(capacity) == 0:
                capacity[j] = queue[0]
                queue.pop(0)
                queue.append(jobs[x][1])
            else:
                queue.pop(0)
                queue.append(jobs[x][1])
                drop += 1
            x += 1

        i += 1

    total_time += max(capacity)+i-1

    return ' '.join([str(total_time), str(drop)])

print(getresult())


