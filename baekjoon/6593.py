'''
Level: G5
Time: 20m41s
'''
import sys
from typing import List, Tuple
from collections import deque
input = lambda: sys.stdin.readline().strip()

def bfs(board: List[List[str]], size: Tuple[int, int, int], start_point: Tuple[int, int, int]):
    L, R, C = size
    s_i, s_j, s_k = start_point

    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    visited[s_i][s_j][s_k] = True
    queue = deque([(*start_point, 0)])

    while queue:
        cur_i, cur_j, cur_k, dist = queue.popleft()
        if board[cur_i][cur_j][cur_k] == 'E':
            return dist

        for di, dj, dk in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            next_i = cur_i + di
            next_j = cur_j + dj
            next_k = cur_k + dk

            if not (0<=next_i<L and 0<=next_j<R and 0<=next_k<C):
                continue
            if board[next_i][next_j][next_k] == '#':
                continue
            if visited[next_i][next_j][next_k]:
                continue

            visited[next_i][next_j][next_k] = True
            queue.append((next_i, next_j, next_k, dist+1))

    return -1


def solution(L: int, R: int, C: int, board: List[List[str]]):
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k] == 'S':
                    return bfs(board, (L, R, C), (i, j, k))


if __name__ == "__main__":
    while True:
        L, R, C = list(map(int, input().split()))
        if L==0 and R==0 and C==0:
            break

        board = []
        for _ in range(L):
            floor = [input() for _ in range(R)]
            board.append(floor)
            input()

        answer = solution(L, R, C, board)
        if answer >= 0:
            print(f"Escaped in {answer} minute(s).")
        else:
            print("Trapped!")
