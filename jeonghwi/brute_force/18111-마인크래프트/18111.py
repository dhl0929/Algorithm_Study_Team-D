from sys import stdin
stdin = open("input.txt")

N, M, B = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]

min_h = 501
max_h = -1

# 가장 높은 위치와 가장 낮은 위치 설정
for i in range(N):
    for j in range(M):
        min_h = min(min_h, maps[i][j])
        max_h = max(max_h, maps[i][j])

def solution(N, M, B, maps):
    # 가장 낮은층 -> 가장 높은층을 하나하나씩 체크
    ans_time = float("inf")
    ans_height = 0
    for h in range(min_h, max_h+1):
        gt = 0
        sb = 0
        rb = 0
        for i in range(N):
            for j in range(M):
                # 현재 블럭이 목표 높이보다 낮다면 쌓아야함
                if maps[i][j] < h:
                    sb += (h - maps[i][j])
                    gt += (h - maps[i][j])
                # 현재 블럭이 목표 높이보다 높다면 없애야함
                elif maps[i][j] > h:
                    rb += (maps[i][j] - h)
                    gt += (maps[i][j] - h) * 2
                # 같다면 그냥 진행
                else:
                    continue

        if (B + rb) - sb >= 0: # 원래 갖고있던 블럭 수랑 채워지는 블럭(rb)을 더해서 소모되는 블럭(sb)의 수가 0이상일 때 체크
            if ans_time > gt:
                ans_time = gt
                ans_height = h
            elif ans_time == gt:
                ans_height = h


    return ans_time, ans_height

print(*solution(N, M, B, maps))