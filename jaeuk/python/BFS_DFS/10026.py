from collections import deque
n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
second_graph = [row[:] for row in graph]
for lst in second_graph:
    for i in range(len(lst)):
        if lst[i] == 'R':
            lst[i] = 'G'

def bfs(y, x, color, graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([[y, x]])
    graph[y][x] = 'X'
    size = 0
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == color:
                queue.append([ny, nx])
                graph[ny][nx] = 'X'
                size += 1
    return size

result = {c: [] for c in ["R", "G", "B"]}
for x in range(n):
    for y in range(n):
        if graph[y][x] == "R":
            g_size = bfs(y, x, "R", graph)
            result['R'].append(g_size)
        elif graph[y][x] == 'G':
            r_size = bfs(y, x, "G", graph)
            result['G'].append(r_size)
        elif graph[y][x] == 'B':
            b_size = bfs(y, x, "B", graph)
            result['B'].append(b_size)

second_result = {c: [] for c in ["G", "B"]}
for x in range(n):
    for y in range(n):
        if second_graph[y][x] == 'G':
            r_size = bfs(y, x, "G", second_graph)
            second_result['G'].append(r_size)
        elif second_graph[y][x] == 'B':
            b_size = bfs(y, x, "B", second_graph)
            second_result['B'].append(b_size)

cnt = 0
for lst in result.values():
    cnt += len(lst)

re_cnt = 0
for lst in second_result.values():
    re_cnt += len(lst)

print(cnt, re_cnt)