'''
Level: S3
Time: 13m20s
'''
import sys
input = lambda: sys.stdin.readline().strip()

if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    A = sorted([0] + list(map(int, input().split())))
    B = sorted([(A[i+1]-A[i], i) for i in range(N)])
    print(sum(B[i][0] for i in range(N-K)))