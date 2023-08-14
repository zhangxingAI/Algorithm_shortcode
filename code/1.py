def reverse(n):
    sequence = list(range(1, n+1))
    steps = []
    for i in range(1, n//2+1):
        if i+1 == n-i+1:
            steps.append((i, i, i + 1))
        else:
            steps.append((i,i,n-i+1))
            sequence[i-1], sequence[i], sequence[n-i] = sequence[i], sequence[n-i], sequence[i-1]
            steps.append((i, i, i+1))
            sequence[i], sequence[i+1] = sequence[i+1], sequence[i]

    print(len(steps))
    for step in steps:
        print(''.join(map(str, step)))

n = int(input())

reverse(n)