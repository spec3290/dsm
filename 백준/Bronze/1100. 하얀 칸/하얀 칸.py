import sys

board = []
cnt = 0

for _ in range(8):
    row = list(sys.stdin.readline().strip())
    board.append(row)

for n in range(8):
    for i in range(8):
        if (n+i) % 2 == 0:
            if(board[i][n] == "F"):
                cnt+=1
print(cnt)