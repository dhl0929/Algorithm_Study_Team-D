from collections import deque
def solution(n, computers):
    visited = [False] * n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for idx, j in enumerate(computers[i]):
            if i != idx and j == 1:
                graph[i].append(idx)

    def bfs(visited, graph, start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            v = queue.popleft()
            
            for i in graph[v]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = True

    
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(visited, graph, i)
            count += 1

    return count