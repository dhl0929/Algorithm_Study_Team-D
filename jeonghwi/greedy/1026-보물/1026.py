from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

def solution(n, A, B):
    ans = 0
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A,B):
        ans += a*b
    
    return ans

print(solution(n, A, B))