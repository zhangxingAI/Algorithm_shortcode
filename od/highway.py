D = int(input())
N = int(input())
charge_pos = [[0,0] for i in range(N+2)]
charge_pos[0][0] = 0
charge_pos[0][1] = 0

for i in range(1,N+1):
    u, v = map(int, input().split(' '))
    charge_pos[i][0] = u
    charge_pos[i][1] = v

charge_pos[N+1][0] = D
charge_pos[N+1][1] = 0

dp = [float('inf') for i in range(N+2)]
dp[0] = 0
flag = True
res = 0
for i in range(1, N+2):
    j = i-1
    while (j >= 0):
        if charge_pos[i][0] -charge_pos[j][0] > 1000:
            break
        else:
            dp[i] = min(dp[i], dp[j] + charge_pos[i][1] + 1)
        j -= 1
    if dp[i] == float('inf'):
        print(-1)
        flag = False
        break
if flag:
    print(int(dp[N+1] + D/100 -1))



