n = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ["L", "R", "U", "D"]

# sol1
moves = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

for plan in plans:
    dx, dy = moves[plan]
    nx, ny = x + dx, y + dy
    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny



# sol2
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or nx > n or ny < 1 or ny > n:
#         continue

#     x, y = nx, ny
#     print(x, y)


# sol2
# def system(x, y, plan):
#     if plan == "U":
#         nx = x - 1
#         if 0 < nx < n:
#             x = nx
#     elif plan == "D":
#         nx = x + 1
#         if 0 < nx < n:
#             x = nx
#     elif plan == "R":
#         ny = y + 1
#         if 0 < ny < n:
#             y = ny
#     elif plan == "L":
#         ny = y - 1
#         if 0 < ny < n:
#             y = ny
#     return x, y


# for plan in plans:
#     x, y = system(x, y, plan)
#     print(x, y)