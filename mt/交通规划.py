n, T = map(int, input().split(" "))
data = [[i+1] for i in range(n)]

ans = []
for _ in range(T):
    line = input().strip().split(" ")
    op, pos = line[0], int(line[1])
    if op == 'L':
        data[pos-1].append(pos-1)
    if op == 'R':
        data[pos - 1].append(pos + 1)
    if op == 'Q':
        ans.append([min(data[pos - 1]),max(data[pos - 1])])
for j in ans:
    print(str(j[0])+' '+str(j[1]))

