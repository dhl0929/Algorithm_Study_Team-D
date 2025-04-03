r, c = map(int, input().split())
board = [input() for _ in range(r)]

cnt = []
for a in range(r-7):
    for b in range(c-7):
        white = 0
        black = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i + j) % 2 == 0:
                    if board[i][j] != "W":
                        black += 1
                    else:
                        white += 1
                else:
                    if board[i][j] != "W":
                        white += 1
                    else:
                        black += 1
                    

        cnt.append(white)
        cnt.append(black)
print(min(cnt))