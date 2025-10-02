'''
Level: S3
Time: 
'''

import sys
input = sys.stdin.readline

def solution(N, genes_1, genes_2):
    first = 1
    set_1, set_2 = set(), set()
    for i in range(N):
        set_1.add(genes_1[i])
        set_2.add(genes_2[i])

        if set_1 == set_2:
            print(f"{first}-{i+1}", end=' ')
            set_1, set_2 = set(), set()
            first = i+2


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())
        genes_1 = list(map(int, input().split()))
        genes_2 = list(map(int, input().split()))
        solution(N, genes_1, genes_2)
