'''
Level: S3
Time: 08m15s
'''

import sys
input = sys.stdin.readline

def solution(N):
    snowflakes = dict()
    for _ in range(N):
        line = list(map(int, input().split()))
        line = tuple(sorted(line))
        if line in snowflakes:
            return True
        else:
            snowflakes[line] = 1
    return False


if __name__ == "__main__":
    N = int(input())

    if solution(N):
        print("Twin snowflakes found.")
    else:
        print("No two snowflakes are alike.")