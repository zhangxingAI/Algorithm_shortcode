n, k = map(int, input().split(' '))
p = [int(_) for _ in input().split(' ')]
sz = n
fr = [0] * n
nt = [0] * n
for i in range(n):
    fr[i] = (i + 1) % n
    nt[i] = (i - 1 + n) % n
ans = []
now = 0
while sz > 0:
    p[now] -= 1
    if p[now] == 0:
        ans.append(now + 1)
        fr[nt[now]] = fr[now]
        nt[fr[now]] = nt[now]
        sz -= 1
    if sz == 0:
        break
    now = fr[now]
    u = k % sz
    u = (u - 1 + sz) % sz
    while u > 0:
        u -= 1
        now = fr[now]
print(" ".join(str(i) for i in ans))

