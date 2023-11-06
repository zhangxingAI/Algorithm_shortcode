'''
题目

输入一串方波信号，求取最长的完全连续交替方波信号，并将其输出，
如果有相同长度的交替方波信号，输出任一即可，方波信号高位用1标识，低位用0标识如图：

说明：

1.一个完整的信号一定以0开始然后以0结尾，
即 010是一个完整的信号，但101，1010，0101 不是
2. 输入的一串方波信号是由一个或多个完整信号组成
3. 两个相邻信号之间可能有0个或多个低位，如0110010，011000010
4. 同一个信号中可以有连续的高位，如01110101011110001010 前14为是一个具有连续高位的信号
5.完全连续交替方波是指10 交替，如01010是完全连续交替方波，0110不是

输入
输入信号字符串（长度大于等于3 且小于等于 1024）
注：输入总是合法的，不考虑异常情况

输出
输出最长的完全连续交替方波信号串
若不存在完全连续交替方波信号串输出-1

input
0010101010110000101000010

output
01010
'''


def solve(str_num):
    ls = []
    start0 = []
    n = len(str_num)
    i = 0
    while i < n-2:
        if str_num[i] + str_num[i+1] == 0 and str_num[i+2] == 1:
            start0.append(i+1)
            i += 3
        i += 1
    for i in start0:
        curr = []
        for _ in range(n):
            if str_num[i] == 0 and i == n-1:
                curr.append(str_num[i])
                if len(ls) < len(curr):
                    ls = curr
                break
            elif str_num[i] == 0 and str_num[i+1] == 1:
                curr.append(str_num[i])
                curr.append(str_num[i + 1])
                i += 2
            elif str_num[i] == 0 and str_num[i+1] == 0:
                curr.append(str_num[i])
                if len(ls) < len(curr):
                    ls = curr
                break
            else:
                curr = []
                break
    if len(ls) >3:
        print(ls)
    else:
        print('-1')

str_num = [int(x) for x in input()]
solve(str_num)


