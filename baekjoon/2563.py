import sys

N = int(sys.stdin.readline())
board = [[0]*101 for _ in range(101)]

for _ in range(N):
    x1, y1 = list(map(int, sys.stdin.readline().split()))
    for dy in range(10):
        for dx in range(10):
            board[y1+dy][x1+dx] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if board[i][j]:
            cnt += 1
print(cnt)