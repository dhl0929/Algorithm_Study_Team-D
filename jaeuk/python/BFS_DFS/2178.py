from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([[y, x]])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                #graph[y][x] = 0
                queue.append([ny, nx])

    return graph[n - 1][m - 1]

print(bfs(0, 0))
