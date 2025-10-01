'''
Level: S5
Time: 09m58s
'''

import sys
input = sys.stdin.readline

def solution(N, rates):
    if N<=1:
        return 0

    max_price = 0    
    for i in range(N):
        for j in range(i+1, N):
            max_price = max(max_price, rates[j]-rates[i])
    return max_price


if __name__ == "__main__":
    N = int(input())
    rates = list(map(int, input().split()))

    print(solution(N, rates))