mod = 10**9 +7
def max_digit(n):
    ls = list(str(n))
    return max([int(i) for i in ls])

def sum_of_max_digit(l,r):
    total = 0
    for i in range(l,r+1):
        total += max_digit(i)
    return total%mod

l,r = map(int, input().split())

res = sum_of_max_digit(l,r)
print(res)
