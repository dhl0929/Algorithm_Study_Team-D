from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, cnt):
    queue = deque([[x, y]])
    graph[x][y] = cnt
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = cnt
                size += 1
    return size

cnt = 2
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            size = bfs(i, j, cnt)
            result.append(size)
            cnt += 1

result.sort()
print(len(result))
for i in result:
    print(i)
