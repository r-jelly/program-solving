'''
Level: S2
Time:
'''
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def solution(nums, K):
    if len(nums) < K:
        return 1
    
    queue = deque(nums)
    while len(queue) > K:
        cur_first = queue.popleft()
        for _ in range(K-1):
            queue.popleft()
        queue.append(cur_first)
    return queue[0]


if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    nums = [*range(1, N+1)]
    print(solution(nums, K))

        