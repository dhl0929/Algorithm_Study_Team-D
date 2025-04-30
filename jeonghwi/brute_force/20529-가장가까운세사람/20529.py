from sys import stdin
stdin = open("input.txt")

T = int(stdin.readline())

MBTI = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
        "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
MBTI_Dict = {M:i for i, M in enumerate(MBTI)}
mat = [[0 for _ in range(16)] for _ in range(16)] # MBTI마다의 거리

def calc_dist(a, b):
    count = 0
    for i, c in enumerate(a):
        if c != b[i]:
            count += 1
    return count

# init matrix
for i in range(16):
    for j in range(16):
        mat[i][j] = calc_dist(MBTI[i], MBTI[j])

for _ in range(T):
    N = int(stdin.readline())
    
    MBTIs = stdin.readline().split()
    min_dist = float("inf") # 가장 가까운 애들이니까 최소 거리여야함

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                A_i = MBTI_Dict[MBTIs[i]]
                B_i = MBTI_Dict[MBTIs[j]]
                C_i = MBTI_Dict[MBTIs[k]]

                AB = mat[A_i][B_i]
                BC = mat[B_i][C_i]
                AC = mat[A_i][C_i]

        min_dist = min(min_dist, AB + BC + AC)

    print(min_dist)