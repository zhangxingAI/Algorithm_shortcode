n = int(input())
a = map(int, input().split(' '))
num_set = set()

count = 0
for i in a:
    num_set.add(i)

for i in num_set:
    for j in num_set:
        num = set()
        num = set.add(i)
        for k in num:
            if i == j or i ==k or j ==k:
                continue
            elif j % k == 0 or k % j == 0:
                count += 1
                num.add(j)
print(count/2)




