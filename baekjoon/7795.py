'''
Level: S3
Time: 06m53s
'''

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = list(map(int, sys.stdin.readline().split()))
    nums_a = list(map(int, sys.stdin.readline().split()))
    nums_b = list(map(int, sys.stdin.readline().split()))

    nums_a.sort(reverse=True)
    nums_b.sort(reverse=True)

    answer, idx_b = 0, 0
    for idx_a in range(N):
        while idx_b<M:
            if nums_a[idx_a] <= nums_b[idx_b]:
                idx_b += 1
            else:
                break
        answer += M-idx_b
    print(answer)
