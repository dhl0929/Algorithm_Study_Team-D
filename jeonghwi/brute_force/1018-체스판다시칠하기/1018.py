from sys import stdin
from copy import deepcopy
#stdin = open('input.txt')

# n 세로, m 가로
n, m = map(int,stdin.readline().split())

board = [list(stdin.readline().rstrip()) for _ in range(n)]

bw = {"B":"W", "W":"B"}

def count_repaint(new_board, count):
    
    for i in range(0,7):
        for j in range(0,7):
            now = new_board[i][j]
            if now == new_board[i][j+1]:
                count+=1
                new_board[i][j+1] = bw[now]
            
            if now == new_board[i+1][j]:
                count+=1
                new_board[i+1][j] = bw[now]
    if new_board[7][7] == new_board[7][6]:
        new_board[7][7] = bw[new_board[7][7]]
        count+=1
    # 가장 마지막꺼 체크
    return count

ny, nx = n-8, m-8
min_count = float("inf")
for y in range(ny+1):
    for x in range(nx+1):
        new_board = []
        for i in range(y,y+8):
            new_board.append(board[i][x:x+8])
        new_board_2 = deepcopy(new_board)
        new_board_2[0][0]=bw[new_board_2[0][0]]
        min_count = min(min_count, count_repaint(new_board, 0))
        min_count = min(min_count, count_repaint(new_board_2, 1))
        
print(min_count)