n, m , q = map(int, input().strip().split(' '))
s = [int(_) for _ in input().strip().split(' ')]
f = []
ans = []
flag = True
for i in range(4):
    f.append([int(_) for _ in input().strip().split(' ')])
g = []
for i in range(int(m)):
    g.append([int(_) for _ in input().strip().split(' ')])
while flag:
    try:
        x, y, z = map(int, input().strip().split(' '))
        print(f[y-1][z-1], int(g[x-1][z-1]),int(s[z-1]))
        if f[y-1][z-1] == 1 and g[x-1][z-1] == 1:
            ans.append("Help yourself")
        if f[y-1][z-1] == 0 and g[x-1][z-1] == 1 and s[z-1] == x:
            ans.append("Ask for help")
        if f[y-1][z-1] == 1 and g[x-1][z-1] == 0 and s[z-1] == x:
            ans.append("Ask for help")
        else:
            ans.append('Impossible')
    except:
        flag = False
for i in ans:
    print(i)