import math

def is_perfect_square(num):
    sqrt = int(math.sqrt(num))
    return sqrt * sqrt ==num
def dfs(node, parents, graph, values, visited):
    visited[node] = True
    red_count = 0

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if is_perfect_square(values[node] * values[neighbor]):
                red_count += 1
                red_count += dfs(neighbor, node, graph, values, visited)
    return red_count

def max_red_nodes(graph, values):
    n = len(graph)
    visited = [False] * n
    max_red = 0

    for i in range(n):
        if not visited[i]:
            red_count = dfs(i, -1, graph, values, visited)
            max_red = max(max_red, red_count)

    return  max_red

edges = []
n = int(input())
values = [int(i) for i in input().split(' ')]
for _ in range(n-1):
    u, v = map(int, input().split(' '))
    edges.append((u-1, v-1))

graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

result = max_red_nodes(graph, values)
print(result)