
T = int(input())
ans = []
for _ in range(T):
    n, a, b = map(int, input().strip().split(" "))
    mean = (a+b)//(n)
    while a > mean:
        a -= mean
    while b > mean:
        b -= mean
    ans.append(max(a,b))
for j in ans:
    print(j)