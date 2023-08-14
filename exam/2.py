def solv():
    n = int(input())
    s = [int(i) for i in input().split(' ')]
    x, y = map(int, input().split(' '))
    res = 0
    sum_d = [0]
    for i in range(n):
        res += s[i]
        sum_d.append(res)
    d = abs(sum_d[y-1] - sum_d[x-1])
    cicle_d = sum_d[-1] - d
    print(min(d, cicle_d))
    return
solv()

