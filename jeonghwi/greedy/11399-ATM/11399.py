from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())
plist = list(map(int,stdin.readline().split()))

def solution(n, plist):
    ans = 0
    plist.sort()
    memo = [0 for _ in range(n)]
    memo[0] = plist[0]
    for i in range(1, n):
        memo[i] = memo[i-1] + plist[i]
    return sum(memo)
print(solution(n, plist))    
