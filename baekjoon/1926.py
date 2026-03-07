'''
Level: S1
Time: 15m11s
'''
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def bfs(painting, visited, point: tuple[int, int]):
    y, x = point
    queue = deque([point])
    visited[y][x] = True
    area = 0

    while queue:
        cur_y, cur_x = queue.popleft()
        area += 1

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_y, next_x = cur_y+dy, cur_x+dx
            if 0<=next_y<len(painting) and 0<=next_x<len(painting[0]):
                if visited[next_y][next_x] or painting[next_y][next_x] == 0:
                    continue

                visited[next_y][next_x] = True
                queue.append((next_y, next_x))
    return area


    

def solution(painting, n, m):
    visited = [[False]*m for _ in range(n)]
    num_paint, max_area = 0, 0
    for i in range(n):
        for j in range(m):
            if painting[i][j] == 1 and not visited[i][j]:
                area = bfs(painting, visited, (i, j))
                max_area = max(area, max_area)
                num_paint += 1

    return num_paint, max_area


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    painting = [list(map(int, input().split())) for _ in range(n)]
    num_paint, max_area = solution(painting, n, m)
    print(num_paint)
    print(max_area)