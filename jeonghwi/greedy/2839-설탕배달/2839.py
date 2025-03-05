from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

# 최대한 5킬로그램 봉지를 다 가져가고, 만약 딱 맞추지 못할 시 5kg -1 하고 3kg + 1한다
def solution(n):
    
    # 5로 먼저 나누기
    init = n//5

    if n%5 == 0:
        return init

    while True:
        if init < 0: # 5킬로를 안씀에도 불구하고 안됐을 경우
            return -1 
        rem = n - (5 * init)
        
        if rem % 3 == 0:
            return init + (rem // 3)
        else:
            init -= 1

print(solution(n))
