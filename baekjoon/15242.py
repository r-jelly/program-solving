'''
Level: S1
Time: 14m58s
'''
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def solution(start: tuple[int, int], target: tuple[int, int]):
    visited = [[False for _ in range(8)] for _ in range(8)]
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    queue = deque([(*start, 0)])
    visited[start[0]][start[1]] = True

    while queue:
        cur_row, cur_col, cur_move = queue.popleft()
        if target[0] == cur_row and target[1] == cur_col:
            return cur_move
        
        for drow, dcol in moves:
            if not (0<=cur_row+drow<8 and 0<=cur_col+dcol<8):
                continue
            if visited[cur_row+drow][cur_col+dcol]:
                continue

            queue.append((cur_row+drow, cur_col+dcol, cur_move+1))
            visited[cur_row+drow][cur_col+dcol] = True

    return -1

if __name__ == "__main__":
    start = input()
    target = input()

    alp_to_num = {alp: i for i, alp in enumerate('abcdefgh')}
    start_pos = (alp_to_num[start[0]], int(start[1])-1)
    target_pos = (alp_to_num[target[0]], int(target[1])-1)

    print(solution(start_pos, target_pos))