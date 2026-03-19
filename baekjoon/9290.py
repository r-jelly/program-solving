'''
Level: S4
Time: 13m32s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

def solution(board: List[str], user_piece: str):
    # 이기는 경우: 가로줄, 세로줄, 대각선
    for i in range(3):
        line = board[i]
        if line[0] == line[1] and line[0] == user_piece:
            point = (i, 2)
        elif line[0] == line[2] and line[0] == user_piece:
            point = (i, 1)
        elif line[1] == line[2] and line[1] == user_piece:
            point = (i, 0)
    
    for i, (x1, x2, x3) in enumerate(zip(board[0], board[1], board[2])):
        if x1 == x2 and x1 == user_piece:
            point = (2, i)
        elif x1 == x3 and x1 == user_piece:
            point = (1, i)
        elif x2 == x3 and x2 == user_piece:
            point = (0, i)
    
    if board[1][1] == board[0][0] and board[1][1] == user_piece:
        point = (2, 2)
    elif board[1][1] == board[2][2] and board[1][1] == user_piece:
        point = (0, 0)
    elif board[0][0] == board[2][2] and board[0][0] == user_piece:
        point = (1, 1)

    if board[1][1] == board[0][2] and board[1][1] == user_piece:
        point = (2, 0)
    elif board[1][1] == board[2][0] and board[1][1] == user_piece:
        point = (0, 2)
    elif board[0][2] == board[2][0] and board[0][2] == user_piece:
        point = (1, 1)

    board[point[0]][point[1]] = user_piece
    for i in range(3):
        print(''.join(board[i]))


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        board = [list(input()) for _ in range(3)]
        user_piece = input()

        print(f"Case {i+1}:")
        solution(board, user_piece)