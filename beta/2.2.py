def color_var(matrix, query):
    result = []

    for q in query:
        x1, y1, x2, y2 = q
        color = set()

        for i in range(x1-1,x2):
            for j in range(y1-1, y2):
                color.add(matrix[i][j])

        result.append(len(color))
    return result

n,m = map(int, input().split(' '))
matrix = []
for _ in range(n):
    row = input().split()
    matrix.append(row)

q = int(input())
query = []
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split(' '))
    query.append((x1, y1, x2, y2))

result = color_var(matrix, query)
for r in result:
    print(r)