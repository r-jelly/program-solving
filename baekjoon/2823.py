'''
Level: S2
Time: 16m40s
'''

import sys
input = sys.stdin.readline

def solution(R, C, board):
    roads = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                roads.append((i, j))

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row, col in roads:
        cnt = 0
        for dx, dy in move:
            if row+dx < 0 or row+dx >= R or col+dy < 0 or col+dy >=C:
                continue
            if board[row+dx][col+dy] == '.':
                cnt += 1
        if cnt < 2:
            return False

    return True


if __name__ == '__main__':
    R, C = list(map(int, input().split()))

    board = []
    for _ in range(R):
        line = list(input().strip())
        board.append(line)

    if solution(R, C, board):
        print("0")
    else:
        print("1")