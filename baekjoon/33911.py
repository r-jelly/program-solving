'''
Level: S3
Time: 1h06m51s
'''

import sys
from itertools import chain
input = sys.stdin.readline


def can_maximum(cnt_nums, num):
    for i in range(num+1, 101):
        if cnt_nums[i] == 1:
            return False
    return True


def solution(cnt_nums, cur_num, length=3):
    if length < 1:
        return 0

    answer = 0
    for i in reversed(range(length, cur_num)):
        if not can_maximum(cnt_nums, i):
            continue
        
        if cnt_nums[i] == 0:
            if length == 3:
                answer += (i-1) * (i-2) // 2
            elif length == 2:
                answer += (i-1)
            elif length == 1:
                answer += 1
        else:
            tmp = cnt_nums[i] 
            cnt_nums[i] = 0
            answer += solution(cnt_nums, i, length-1)
            cnt_nums[i] = tmp

    return answer


if __name__ == "__main__":
    N = int(input())
    teams = [list(map(int, input().split())) for _ in range(N)]
    all_nums = chain(*teams)
    
    cnt_nums = [0] * 110
    for num in all_nums:
        cnt_nums[num] += 1

    print(solution(cnt_nums, 101, 3))