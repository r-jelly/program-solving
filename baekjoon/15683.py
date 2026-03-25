'''
Level: G3
Time: 42m06s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

cctv_direction = {
    1: [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]],
    2: [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    3: [
        [(-1, 0), (0, 1)],
        [(0, 1), (1, 0)],
        [(1, 0), (0, -1)],
        [(0, -1), (-1, 0)]
    ],
    4: [
        [(-1, 0), (0, 1), (0, -1)],
        [(0, 1), (1, 0), (-1, 0)],
        [(1, 0), (0, -1), (0, 1)],
        [(0, -1), (-1, 0), (1, 0)]
    ],
    5: [[(1, 0), (-1, 0), (0, 1), (0, -1)]]
}

def set_cctv(board, points, direction):
    p_i, p_j = points
    di, dj = direction

    next_i, next_j = p_i+di, p_j+dj
    while 0<=next_i<len(board) and 0<=next_j<len(board[0]):
        if board[next_i][next_j] == 6:
            break
        elif board[next_i][next_j] > 0:
            pass
        else:
            board[next_i][next_j] -= 1
        next_i, next_j = next_i+di, next_j+dj
    return board


def del_cctv(board, points, direction):
    p_i, p_j = points
    di, dj = direction

    next_i, next_j = p_i+di, p_j+dj
    while (0<=next_i<len(board) and 0<=next_j<len(board[0])):
        if board[next_i][next_j] == 6:
            break
        elif board[next_i][next_j] > 0:
            pass
        else:
            board[next_i][next_j] += 1
        next_i, next_j = next_i+di, next_j+dj
    return board


def dfs(board, points, cur_idx):
    if cur_idx >= len(points):
        area = 0
        for line in board:
            for p in line:
                if p == 0:
                    area += 1
        return area

    min_area = float('inf')
    for i in range(cur_idx, len(points)):
        cur_point = points[i]
        cctv_type = board[cur_point[0]][cur_point[1]]

        for directions in cctv_direction[cctv_type]:
            for direction in directions:
                    board = set_cctv(board, cur_point, direction)
            cur_area = dfs(board, points, i+1)
            min_area = min(min_area, cur_area)
            for direction in directions:
                board = del_cctv(board, cur_point, direction)

    return min_area
        

def solution(board: List[List[int]], N: int, M: int):
    cctv_points = []
    for i in range(N):
        for j in range(M):
            if board[i][j] >= 1 and board[i][j] <= 5:
                cctv_points.append((i, j))
    return dfs(board, cctv_points, 0)


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = solution(board, N, M)
    print(answer)