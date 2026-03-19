'''
Level: G3
Time: 44m28s
'''
import sys
from typing import List, Tuple
from collections import deque
input = lambda: sys.stdin.readline().strip()


def dfs(board: List[List[str]], start: int, stack: List[str], count_not_S: int):
    if count_not_S >= 4:
        return 0

    if len(stack) == 7:
        return check_available(stack)

    available_count = 0
    for idx in range(start, 25):
        cur_i, cur_j = idx//5, idx%5

        stack.append((cur_i, cur_j))
        available_count += dfs(board, idx+1, stack, count_not_S+int(board[cur_i][cur_j]!='S'))
        stack.pop()
    return available_count


def check_available(point_list: List[Tuple[int, int]]):
    visited = [False] * len(point_list)
    visited[0] = True
    queue = deque([point_list[0]])

    while queue:
        cur_i, cur_j = queue.popleft()

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_i, next_j = cur_i + di, cur_j + dj
            if not (0<=next_i<5 and 0<=next_j<5):
                continue
            if (next_i, next_j) not in point_list:
                continue
        
            cur_idx = point_list.index((next_i, next_j))
            if visited[cur_idx]:
                continue
            visited[cur_idx] = True
            queue.append((next_i, next_j))

    if all(visited):
        return 1
    else:
        return 0


if __name__ == "__main__":
    board = [input() for _ in range(5)]
    answer = dfs(board, 0, [], 0)
    print(answer)