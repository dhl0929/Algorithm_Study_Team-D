from sys import stdin
stdin = open("input.txt","r")

# 종민이는 현재 흑돌로 플레이
n = int(stdin.readline())
maps = [[c for c in stdin.readline().rstrip()] for _ in range(n)]
directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

def check_stone(y, x, dir):
    # 들어온 방향으로 끝까지 체크
    count = 0
    ny = y+dir[0]
    nx = x+dir[1]
    while True:
        if (0 <= ny < n) and (0 <= nx < n):
            if maps[ny][nx] == "W":
                count += 1 # 백돌이므로 증가
            elif maps[ny][nx] == "B": # 이 함수 종료조건 (흑돌을 마주침)
                return count
            elif maps[ny][nx] == ".": # W로 시작해서 중간에 .이 있는 경우 B까지 도달 X -> 놓을 수 없는 공간
                return 0
            ny += dir[0]
            nx += dir[1]

        else: # 범위를 넘어갈 때 까지 흑돌 못 마주침
            return False

def reverse_stone(y, x):
    reverse_count = 0
    for dir in directions:
        ny = y+dir[0]
        nx = x+dir[1]
        # 다음경로가 범위내에 있는지와 함께 백돌인지 판단
        if (0 <= ny < n) and (0 <= nx < n):
            if maps[ny][nx] == "W":
                count = check_stone(y, x, dir) # 놓을 수 있는 위치인지 체크와 함께 거리계산
                if not count: # 범위를 넘어갈 때 까지 흑돌을 못 봤을 때, 정답에 더하지 않고 넘어감
                    continue

                reverse_count += count # 흑돌 마주치면 더해줌
        else:
            continue

    return reverse_count

def solution(n, maps):
    # 놓을 수 있는 위치 선확인
    ans_dirs = [-1, -1]
    ans_stones = -1

    for i in range(n):
        for j in range(n):
            if maps[i][j] == ".":
                reverse_count = reverse_stone(i, j)
                if ans_stones < reverse_count:
                    ans_stones = reverse_count
                    ans_dirs = [i, j]
                elif ans_stones == reverse_count:
                    if i < ans_dirs[0]:
                        ans_dirs = [i, j]
                    elif i == ans_dirs[0]:
                        if j < ans_dirs[1]:
                            ans_dirs = [i, j]
                    
    if ans_stones == 0:
        print("PASS")
        return
    
    print(ans_dirs[1], ans_dirs[0])
    print(ans_stones)

solution(n, maps)


# 빈공간(.) 다음에 빈공간이 이어지고, 그 뒤에 흰돌(W)가 이어진뒤, 검은돌(B)로 끝나는 경우를 생각해야함!!!!