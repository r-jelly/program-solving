'''
Level: S2
Time: 55m12s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()

def solution(butter_info: List[List[int]]) -> int:
    overlap_time = []
    for i in range(1, len(butter_info)):
        x1, h1 = butter_info[i-1]
        x2, h2 = butter_info[i]

        if (x1 + h1//2) < (x2 - h2//2):
            overlap_time.append(-1)
            continue

        min_spread_time = min(h1//2, h2//2)
        x1_right = x1 + min_spread_time
        x2_left = x2 - min_spread_time

        if x1_right < x2_left:
            overlap_time.append(min_spread_time + (x2_left - x1_right) - 1)
        else:
            overlap_time.append(min_spread_time - (x1_right - x2_left)//2 - 1)

    min_time = float('inf')
    for time in overlap_time:
        if time != -1:
            min_time = min(min_time, time)

    if min_time == float('inf'):
        return -1
    else:
        return min_time


if __name__ == "__main__":
    N = int(input())
    butter_info = [list(map(int, input().split())) for _ in range(N)]
    answer = solution(sorted(butter_info, key=lambda x: x[0]))

    if answer >= 0:
        print(answer)
    else:
        print('forever')