import sys
input = sys.stdin.readline

N = int(input())

ans = 0
while N > 0:
    if N % 5 == 0:
        ans += N // 5
        break
    N -= 3
    ans += 1
    if N == 0:
        break
    if N < 0:
        ans = -1
        break

print(ans)