
T = int(input())
for _ in range(T):
    n, a, b = map(int, input().strip().split(" "))
    def check(x):
        r1, r2 = min(a, b), max(a, b)
        cnt = 1
        r2 -= x
        cnt += (r2 // x) + (r1 // x)
        '''一个人分x  其他人x+1， 如果可以就ok'''
        return cnt >= n


    l, r = 0, max(a, b)
    while l < r:
        mid = (l + r + 1) >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(r)