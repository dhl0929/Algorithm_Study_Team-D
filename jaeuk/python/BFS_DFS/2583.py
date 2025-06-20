from collections import deque
n, m, k = map(int, input().split())
graph = [[1] * m for _ in range(n)]
for _ in range(k):
    a, b, c, d = map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            graph[j][i] = 0

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([[y, x]])
    graph[y][x] = 2
    size = 1
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                queue.append([ny, nx])
                graph[ny][nx] = 2
                size += 1
    return size

result = []
for p in range(m):
    for q in range(n):
        if graph[q][p] == 1:
            size = bfs(p, q)
            result.append(size)

result.sort()
print(len(result))
for i in result:
    print(i, end = ' ')