import sys
import math

input = sys.stdin.readline

n, m= map(int, input().split())

# 3. 조합의 수 구하기
answer = math.comb(m, n)

# 4. 원하는 형식으로 출력
print(answer)