n=int(input())
m=int(input())
A=[0]*n
vis=[0]*1000005
dp=[0]*1000005
c1 = [0]*100000
c2 = [0]*100000
s=input().split(' ')
for i in range(n): A[i]=int(s[i-1])
A.sort()
if (n == 1):
    print(1,a[0])
elif (n == 2):
    print(2,min(A[0] * 10, max(a[0], a[1])))
else:
    dp[1] = a[0]
    dp[2] = a[1]
    pre = n
    for i in range(3,n+1):
        c1[i] = dp[i-2]+ a[0] + a[i-1] + a[1] + a[1]
        c2[i] = dp[i-1] + a[0] + min(a[i-1], 10*a[0])
        dp[i] = min(c1[i], c2[i])
        if (dp[i] > m):
            pre = i - 1
            break
        print(pre,dp[pre])