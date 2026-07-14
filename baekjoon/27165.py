'''
Level: S3
Time: 32m57s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

def solution(board: List[int], dice: int):
    unsafe_point = [i for i in range(len(board)) if board[i]==1]

    if len(unsafe_point) > 2:
        pass
    elif len(unsafe_point) == 2:
        if unsafe_point[1] - unsafe_point[0] == dice:
            return unsafe_point
    elif len(unsafe_point) == 1:
        if unsafe_point[0]-dice >= 0:
            if board[unsafe_point[0]-dice] > 2:
                return unsafe_point[0]-dice, unsafe_point[0]
        if unsafe_point[0]+dice < len(board):
            if board[unsafe_point[0]+dice] >= 1:
                return unsafe_point[0], unsafe_point[0]+dice
    else:
        for i in range(len(board)-dice):
            if board[i] > 2 and board[i+dice] > 1:
                return i, i+dice
    
    return -1, -1


if __name__ == "__main__":
    N = int(input())
    a_list = list(map(int, input().split()))
    dice = int(input())

    p1, p2 = solution(a_list, dice)
    if p1 != -1:
        print("YES")
        print(p1, p2)
    else:
        print("NO")