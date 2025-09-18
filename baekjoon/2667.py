'''
Level: S1
Time: 22m53s
'''

import sys
from collections import deque

input = sys.stdin.readline


def bfs(board, start_point):
    N = len(board)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start_point])
    board[start_point[0]][start_point[1]] = 0
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        cnt += 1

        for dx, dy in moves:
            next_x, next_y = x+dx, y+dy
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if not board[next_x][next_y]:
                continue

            board[next_x][next_y] = 0
            queue.append((next_x, next_y))            

    return cnt


if __name__ == "__main__":
    N = int(input())

    board = []
    for _ in range(N):
        line = list(map(int, list(input().strip())))
        board.append(line)

    cnt_list = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                cnt = bfs(board, (i,j))
                cnt_list.append(cnt)
    
    print(len(cnt_list))
    for cnt in sorted(cnt_list):
        print(cnt)