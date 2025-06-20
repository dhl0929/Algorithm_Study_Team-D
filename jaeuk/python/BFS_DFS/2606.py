from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def dfs(graph, visited, start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, visited, i)
    return visited

print(sum(dfs(graph, visited, 1)) - 1)




# def bfs(graph, visited, start):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         visited[v] = True

#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#     return visited

# print(sum(bfs(graph, visited, 1)) - 1)