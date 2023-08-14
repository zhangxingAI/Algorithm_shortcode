st = [set() for _ in range(7)]
for i in range(7):
    arr = [int(_) for _ in input().split()]
    for j in arr[1:]:
        st[i].add(j)
valid = [set() for _ in range(7)]
for i in range(7):
    for j in range(10):
        if j not in st[i]:
            valid [i].add(j)
def cal(x):
    res = 0
    while x:
        x &= (x-1)
        res += 1
    return res

res = 0x3f3f3f3
for i in range(1<<10):
    ok = 1
    for j in range(7):
        now = 0
        for k in range(10):
            if i & (1<<k) and k in valid[j]:
                now = 1
                break
        if not now:
            ok = 0
            break
    if ok:
        res = min(res, cal(i))
print(-1 if res == 0x3f3f3f3 else res)
