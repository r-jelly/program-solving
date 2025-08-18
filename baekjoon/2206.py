import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(N):
    line = list(map(int, list(sys.stdin.readline().strip())))
    board.append(line)

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False]*M for _ in range(N)]
visited_wall = [[False]*M for _ in range(N)]

visited[0][0] = True
queue = deque([(0, 0, 1, True)])
final_depth = -1

while queue:
    row, col, cur_depth, can_break = queue.popleft()
    if row==N-1 and col==M-1:
        final_depth = cur_depth
        break

    for dx, dy in move:
        if not ( (0<=row+dx<N) and (0<=col+dy<M) ):
            continue

        if can_break and visited[row+dx][col+dy]:
            continue
        elif not can_break and visited_wall[row+dx][col+dy]:
            continue

        if board[row+dx][col+dy] == 1:
            if not can_break:
                continue
            else:
                next_break = False
        else:
            next_break = can_break

        if next_break:
            visited[row+dx][col+dy] = True
        else:
            visited_wall[row+dx][col+dy] = True
        queue.append((row+dx, col+dy, cur_depth+1, next_break))

print(final_depth)