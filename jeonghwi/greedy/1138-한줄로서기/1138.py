from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

nlist = list(map(int,stdin.readline().split()))

ans = [-1 for _ in range(n)]

# 빈 공간에 들어가기?
for ind, num in enumerate(nlist):
    count = 0
    for i in range(n):
        if ans[i] == -1:
            if count == num:
                ans[i] = ind+1
            count+=1
            continue

print(*ans)