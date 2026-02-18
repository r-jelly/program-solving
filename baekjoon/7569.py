'''
Level: G5
Time: 27m05s
'''
import sys
from collections import deque
input = sys.stdin.readline

def check_all_good(board):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if board[i][j][k] == 0:
                    return False
    return True


def bfs(board, points, *args):
    queue = deque(points)
    moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    assert len(args) == 3
    M, N, H = args

    cnt = -1
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            for dx, dy, dz in moves:
                if not (0<=x+dx<H and 0<=y+dy<N and 0<=z+dz<M):
                    continue
                if board[x+dx][y+dy][z+dz] == 0:
                    board[x+dx][y+dy][z+dz] = 1
                    queue.append((x+dx, y+dy, z+dz))

    return cnt if check_all_good(board) else -1


if __name__ == "__main__":
    M, N, H = list(map(int, input().split()))
    board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    # 1: 익은 토마토, 0: 안익은 토마토, -1: 토마토 없음
    points = [(x, y, z) for x in range(H) for y in range(N) for z in range(M) if board[x][y][z] == 1]

    print(bfs(board, points, M, N, H))
    