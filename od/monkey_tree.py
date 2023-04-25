n = int(input())
node = [[] for _ in range(n)]
edge = int(input())
for _ in range(edge):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)
b = int(input())
block = set()
for _ in range(b):
    bl = int(input())
    block.add(bl)

queue = [(0, -1)]
ans = []
path = [-1] * n
front = 1
Flag =True
while Flag:
    u, father = queue[front]
    front += 1
    flag = 0
    for i in node[u]:
        if i not in block:
            flag = 1
    if flag == 1:
        for i in node[u]:
            if i != father and i not in block:
                queue.append((i, u))
                path[i] = u
            elif len(node[u]) == 1:
                Flag = False
                p = u
                while p != -1:
                    ans.append(str(p))
                    p = path[p]
                ans.reverse()
                print("->".join(ans))
                break
    else:
        print('NULL')
        Flag =False




