from collections import deque
n = int(input())


def bfs(start_y, start_x, end_y, end_x):
    queue = deque([((start_y, start_x), 0)])
    graph[start_y][start_x] = 1
    way = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
     
    while queue:
        (y, x), idx = queue.popleft()
        if y == end_y and x == end_x:
            return idx
            break

        for dy, dx in way:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < l and 0 <= ny < l and graph[ny][nx] == 0:
                queue.append([(ny, nx), idx + 1])
                graph[ny][nx] = 1



for _ in range(n):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph = [[0] * l for _ in range(l)]

    idx = bfs(start_y, start_x, end_y, end_x)
    print(idx)