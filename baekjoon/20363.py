'''
Level: S4
Time: 13m10s
'''

import sys
input = sys.stdin.readline

def solution(X, Y):
    if X > Y:
        return X+Y+Y//10
    else:
        return X+Y+X//10

if __name__ == "__main__":
    X, Y = list(map(int, input().split()))
    print(solution(X, Y))