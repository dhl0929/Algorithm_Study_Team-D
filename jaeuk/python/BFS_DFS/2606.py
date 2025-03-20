from collections import deque
computers = int(input())
num_pairs = int(input())
pairs = [[] for _ in range(computers + 1)]
visited = [False] * (computers + 1)

for _ in range(num_pairs):
    a, b = map(int, input().split())
    pairs[a].append(b)
    pairs[b].append(a)


def bfs(start, pairs):
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in pairs[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return sum(visited) - 1

print(bfs(1, pairs))