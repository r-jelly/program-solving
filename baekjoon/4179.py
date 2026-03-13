'''
Level: G3
Time: 39m16s
'''
import sys
from collections import deque
from typing import List, Tuple
input = lambda: sys.stdin.readline().strip()

def get_fire_board(board: List[str], point_list: List[Tuple[int, int]], R: int, C: int):
    visited = [[False] * C for _ in range(R)]
    queue = deque([])
    fire_board = [[-1 for _ in range(C)] for _ in range(R)]

    for row, col in point_list:
        visited[row][col] = True
        queue.append(((row, col), 0))
        fire_board[row][col] = 0

    while queue:
        (cur_row, cur_col), level = queue.popleft()
        for drow, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_row = cur_row + drow
            next_col = cur_col + dcol

            if not (0 <= next_row < R and 0 <= next_col < C):
                continue
            if visited[next_row][next_col]:
                continue
            if board[next_row][next_col] == '#':
                continue
            
            visited[next_row][next_col] = True
            fire_board[next_row][next_col] = level + 1
            queue.append(((next_row, next_col), level + 1))
    return fire_board


def solution(board: List[str], init_point: Tuple[int, int], fire_point_list: List[Tuple[int, int]]):
    R, C = len(board), len(board[0])

    # Fire가 특정 위치에 도달하는 최소 시간을 나타내는 지도 제작
    fire_board = get_fire_board(board, fire_point_list, R, C)
    visited = [[False] * C for _ in range(R)]
    visited[init_point[0]][init_point[1]] = True
    queue = deque([(init_point, 0)])

    while queue:
        (cur_row, cur_col), level = queue.popleft()

        # 사람이 가장자리에 도달했다면, 그때까지 걸린 시간을 반환
        if cur_row == 0 or cur_row == R-1 or cur_col == 0 or cur_col == C-1:
            return level

        for drow, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_row = cur_row + drow
            next_col = cur_col + dcol

            if not (0 <= next_row < R and 0 <= next_col < C):
                continue
            if visited[next_row][next_col]:
                continue
            if board[next_row][next_col] == '#':
                continue
            if 0 <= fire_board[next_row][next_col] <= (level + 1):
                continue

            visited[next_row][next_col] = True
            queue.append(((next_row, next_col), level + 1))
    return -1


if __name__ == "__main__":
    # 입출력 처리
    R, C = list(map(int, input().split()))
    board = [input() for _ in range(R)]

    # Fire는 여러 개가 존재할 수 있음
    fire_point_list = []
    for row in range(R):
        for col in range(C):
            if board[row][col] == 'J':
                init_point = (row, col)
            elif board[row][col] == 'F':
                fire_point_list.append((row, col))

    # 사람이 미로 가장자리에 도달하는데 걸리는 시간
    time = solution(board, init_point, fire_point_list)
    if time < 0:
        print("IMPOSSIBLE")
    else:
        print(time+1)