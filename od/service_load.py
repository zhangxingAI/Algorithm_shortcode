d = [0]*1000001
minL = int(1000000)
maxR = int(-1000000)

n = int(input())
for i in range(n):
    l,r = map(int, input().split())
    if l < 0 or l > 1000000 or r < 0 or r > 1000000:
        print('输入值范围[0, 1000000]')
    minL = min(minL, l)
    maxR = max(maxR, r)
    for j in range(l, r+1, 1):
        d[j] += 1
ans = 0
for i in range(minL, maxR+1):
    if d[i] == 0:
        ans += 1
    elif d[i] == 1:
        ans += 3
    elif d[i] > 1:
        ans += 4
print(ans)
