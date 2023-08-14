def min_taste_diff(matrix):
    n = len(matrix)
    m = len(matrix[0])

    total_taste = sum(sum(row) for row in matrix)
    half_total = total_taste//2

    dp = [[0] * (half_total +1) for _ in range(2)]

    for i in range(1, n*m +1):
        row = (i-1)//m
        col = (i-1)%m
        for j in range(half_total+1):
            dp[i%2][j] = dp[(i-1)%2][j]
            if j>= matrix[row][col]:
                dp[i%2][j] = max(dp[i%2][j], dp[(i - m)%2][j - matrix[row][col]] + matrix[row][col])

    s1 = dp[n*m%2][half_total]
    s2 = total_taste- s1
    min_diff = abs(s1-s2)

    return min_diff

n, m = map(int, input().split(' '))
matrix =[]
for _ in range(n):
    row = list(map(int, input().split(' ')))
    matrix.append((row))

result = min_taste_diff(matrix)
print(result)