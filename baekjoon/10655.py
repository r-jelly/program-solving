'''
Level: S3
Time: 16m47s
'''
import sys
from typing import List
input = lambda: sys.stdin.readline().strip()


def solution(point_list: List[List[int]]):
    all_dist = 0
    for i in range(1, len(point_list)):
        all_dist += abs(
            point_list[i-1][0] - point_list[i][0]
        ) + abs(
            point_list[i-1][1] - point_list[i][1]
        )

    diff_list = []
    for i in range(1, len(point_list)-1):
        prev_x, prev_y = point_list[i-1]
        cur_x, cur_y = point_list[i]
        next_x, next_y = point_list[i+1]

        prev_dist = abs(prev_x-cur_x) + abs(prev_y-cur_y)
        next_dist = abs(next_x-cur_x) + abs(next_y-cur_y)
        jump_dist = abs(next_x-prev_x) + abs(next_y-prev_y)
        diff_list.append(prev_dist+next_dist-jump_dist)
    
    return all_dist - max(*diff_list, 0)


if __name__ == "__main__":
    N = int(input())
    point_list = [list(map(int, input().split())) for _ in range(N)]
    answer = solution(point_list)
    print(answer)