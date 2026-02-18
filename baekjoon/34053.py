'''
Level: S3
Time: 15m09s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(board):
    board_sum = 0
    min_num = float('inf')
    for i in range(len(board)):
        for j in range(len(board[i])):
            min_num = min(min_num, board[i][j])
            board_sum += board[i][j]

    return board_sum - min_num


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution(board))
