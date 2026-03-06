'''
Level: S5
Time: 10m35s
'''
import sys
sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().strip()

SWAP = 0

def quick_sort(A, left, right, K):
    if left < right:
        q = partition(A, left, right, K)
        quick_sort(A, left, q-1, K)
        quick_sort(A, q+1, right, K)

def partition(A, p, r, K):
    global SWAP

    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x and SWAP < K:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            SWAP += 1

    if i+1 != r and SWAP < K:
        tmp = A[i+1]
        A[i+1] = A[r]
        A[r] = tmp
        SWAP += 1
    return i+1

if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr)-1, K)
    if SWAP < K:
        print(-1)
    else:
        print(*arr)