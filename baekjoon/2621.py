'''
Level: S3
Time: 31m10s
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

def check_num_continuous(nums: dict):
    prev = None
    for num, count in sorted(nums.items()):
        if count != 1:
            return False
        if prev and int(num)-1 != prev:
            return False
        prev = int(num)
    return True

def check_color_all_same(colors: dict):
    if len(colors) == 1:
        return True
    return False

def solution(cards: list[tuple]) -> int:
    colors, nums = defaultdict(int), defaultdict(int)
    for color, num in cards:
        colors[color] += 1
        nums[int(num)] += 1

    flag_color_all_same = check_color_all_same(colors)
    flag_num_continuous = check_num_continuous(nums)

    if flag_num_continuous:
        if flag_color_all_same:
            return max(nums.keys()) + 900
        else:
            return max(nums.keys()) + 500
    else:
        nums_cnt = sorted(nums.items(), key=lambda x: (x[1], x[0]), reverse=True)
        if len(nums_cnt) <= 2:
            if nums_cnt[0][1] >= 4:
                return int(nums_cnt[0][0]) + 800
            else:
                return int(nums_cnt[0][0]) * 10 + int(nums_cnt[1][0]) + 700
        elif flag_color_all_same:
            return max(nums.keys()) + 600
        elif len(nums_cnt) <= 4:
            if nums_cnt[0][1] == 3:
                return int(nums_cnt[0][0]) + 400
            elif nums_cnt[1][1] == 2:
                return int(nums_cnt[0][0]) * 10 + int(nums_cnt[1][0]) + 300
            else:
                return int(nums_cnt[0][0]) + 200
        else:
            return max(nums.keys()) + 100


if __name__ == "__main__":
    cards = [tuple(input().split()) for _ in range(5)]
    cards = sorted(cards, key=lambda x: x[1])
    print(solution(cards))