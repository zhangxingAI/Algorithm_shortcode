T = int(input())
def solv():
    n =  int(input())
    colors = [int(c) for c in input().split(' ')]
    pres0 = [0 for _ in range(n + 1)]
    pres1 = [0 for _ in range(n + 1)]
    res = [0 for _ in range(n)]
    for i in range(n):
        if colors[i] == 0:
            pres0[i+1] = pres0[i] + 1
            pres1[i + 1] = pres1[i]
        else:
            pres1[i + 1] = pres1[i] + 1
            pres0[i + 1] = pres0[i]
    for i in range(n):
        if colors[i] == 0:
            



