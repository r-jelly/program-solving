'''
Level: S3
Time: 08m35s
'''

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    costs = sorted(list(zip(A, B)))

    for i in range(N):
        if costs[i][0] > costs[i][1]:
            continue
        if costs[i][0] > M:
            continue

        M += costs[i][1] - costs[i][0]

    print(M)