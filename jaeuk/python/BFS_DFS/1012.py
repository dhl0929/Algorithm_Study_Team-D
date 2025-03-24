from collections import deque

def bfs(x, y):
    queue = deque([[x, y]])
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < m and ny >= 0 and ny < n and graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = 0


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
