'''
Level: G5
Time: 13m03s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()


def bfs(board: List[str], visited: List[List[bool]], row: int, col: int, color: str):
    stack = list([(row, col)])
    while stack:
        cur_row, cur_col = stack.pop()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_row = cur_row + dx
            next_col = cur_col + dy

            if not (0<=next_row<len(board) and 0<=next_col<len(board)):
                continue
            if visited[next_row][next_col]:
                continue
            if board[next_row][next_col] not in color:
                continue
            visited[next_row][next_col] = True
            stack.append((next_row, next_col))


def solution(board: List[str]):
    not_blind, blind = 0, 0

    visited = [[False]*len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if visited[i][j]:
                continue
            not_blind += 1
            color = board[i][j]
            bfs(board, visited, i, j, color)

    visited = [[False]*len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if visited[i][j]:
                continue
            blind += 1
            color = 'B' if board[i][j] == 'B' else 'RG'
            bfs(board, visited, i, j, color)

    return not_blind, blind

if __name__ == "__main__":
    N = int(input())
    board = [input() for _ in range(N)]
    print(*solution(board))