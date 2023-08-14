
def solv():
    n = int(input())
    s = [int(i) for i in input().split(' ')]
    x, y = map(int, input().split(' '))
    for i in range(n):
        if s[0] == x and s[1] == y:
            print('YES')
            break
        elif i>0 and s[i] == x and (s[i-1] == y or s[i+1] == y):
            print('YES')
            break
        elif i == n-1:
            print('NO')
    return
solv()


