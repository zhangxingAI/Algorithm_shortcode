T = int(input())
def solv():
    a, b = map(int, input().split(' '))
    s = str(a)
    for i in range(len(s)):
        if int(s[i]) < b:
            print(s[:i] + str(b) + s[i:])
            return
    print(s + str(b))


for i in range(T):
    solv()
