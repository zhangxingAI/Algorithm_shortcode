mod = 10**9 +7
def max_digit(n):
    return int(max(str(n)))
def sum_of_max_digit(l,r):
    total_pre = 0
    curr = 1

    for i in range(l, r + 1):
        total_pre += max_digit(i)


    return total % mod

l,r = map(int, input().split())
res = sum_of_max_digit(l,r)
print(res)
