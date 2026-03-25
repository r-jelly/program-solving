'''
Level: S4
Time: 18m10s
'''
import sys
from itertools import combinations
input = lambda: sys.stdin.readline().strip()

def win_or_lose(is_same: bool, num: int, remain):
    win, not_win = 0, 0
    combin = combinations(remain, 2)
    for i, j in combin:
        if is_same:
            if i != j:
                win += 1
            else:
                if i < num:
                    win += 1
                else:
                    not_win += 1
        else:
            if i == j:
                not_win += 1
            else:
                if (i+j)%10 >= num:
                    not_win += 1
                else:
                    win += 1
    return win, not_win

def solution(n1: int, n2: int):
    remain = [i for i in range(1, 11) if i != n1] + [j for j in range(1, 11) if j != n2]
    if n1 == n2:
        # 땡인 경우
        win, not_win = win_or_lose(True, n1, remain)
    else:
        # 끗인 경우
        win, not_win = win_or_lose(False, (n1+n2)%10, remain)
    print(f"{win/(win+not_win):.3f}")


if __name__ == "__main__":
    A, B = list(map(int, input().split()))
    solution(A, B)