'''
Level: G4
Time: 31m33s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def findFirstGreaterThanOrEqual(array, N, X):
    start, end = 0, N
    while (start < end):
        mid = (start + end) // 2
        if array[mid] > X:
            end = mid
        else:
            start = mid + 1
        
    return start


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, X, Y = list(map(int, input().split()))
        if Y==1:
            if N < X:
                print(*range(1, N+1))
            else:
                print(*range(1, X), *range(X+1, N+2))
        else:
            if N < X:
                print(*range(1, N), X)
            else:
                print(*range(1, N+1))