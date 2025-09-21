'''
Level: S5
'''

import sys
N, M = list(map(int, sys.stdin.readline().split()))

ranks = []
for i in range(N):
    rank = int(sys.stdin.readline())
    ranks.insert(rank-1, i+1)

final_ranks = []
for i in reversed(ranks[:M]):
    rank = int(sys.stdin.readline())
    final_ranks.insert(rank-1, i)

for i in range(3):
    print(final_ranks[i])