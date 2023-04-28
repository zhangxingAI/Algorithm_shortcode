C = int(input())
ans = []
for _ in range(C):
    S = input()
    T = input()
    res, pos = 0, 0
    if len(S) > len(T):
        res = len(S) - len(T)
        pos = len(T)
    else:
        pos = len(S)
    for i in range(pos):
        if S[i] != T[i]:
            res += 1
    ans.append(res)
for j in ans:
    print(j)