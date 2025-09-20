'''
Level: S1
Time: 13m47s
'''

import sys
input = sys.stdin.readline

def solution(N, K, nums):
    start, end = 0, 0
    cnt = 1 if nums[0]==1 else 0
    min_len = float('inf')

    while True:
        if cnt<K:
            end += 1
            if end>=N:
                break
            cnt += 1 if nums[end]==1 else 0
        else:
            min_len = min(min_len, end-start+1)
            cnt -= 1 if nums[start]==1 else 0

            start += 1
            if start>=N:
                break
    return min_len if min_len<=1000000 else -1
            

if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(solution(N, K, nums))