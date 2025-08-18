import sys
N, M = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)

presum_board = []
for i in range(N):
    line = [0]
    for j in range(N):
        next_num = line[-1] + board[i][j]
        line.append(next_num)
    presum_board.append(line)

for _ in range(M):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    cur_sum = 0
    for i in range(x1, x2+1):
        cur_sum += presum_board[i-1][y2] - presum_board[i-1][y1-1]
    print(cur_sum)

# Solved 18m10s