'''
Level: S3
Time: 11m09s
'''
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def solution(ds, ds_num, nums):
    queue = list(reversed([ds_num[idx] for idx in range(len(ds)) if not ds[idx]]))
    if len(queue) >= len(nums):
        return queue[:len(nums)]
    else:
        return queue + nums[:len(nums)-len(queue)]

if __name__ == "__main__":
    N = int(input())
    ds = list(map(int, input().split()))
    ds_num = list(map(int, input().split()))
    M = int(input())
    nums = list(map(int, input().split()))

    print(*solution(ds, ds_num, nums))
