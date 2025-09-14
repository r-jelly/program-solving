'''
Level: S2
Time: 12m42s
'''

import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = A[0]

for i in range(1, N):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))