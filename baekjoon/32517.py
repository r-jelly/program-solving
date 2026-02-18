'''
Level: S3
Time: 30m29s
'''
import sys
input = lambda: sys.stdin.readline().strip()

def solution(B):
    if B[0] == 0:
        return []
    
    A = [0] * len(B)
    A_sum = [0] * len(B)
    A[0], A_sum[0] = B[0], B[0]
    for i in range(1, len(B)):
        if B[i]+1 < A_sum[i-1]/i and B[i]+1 < 1000000000:
            A[i] = B[i] + 1
        elif B[i] >= A_sum[i-1]/i and B[i] >= 1:
            A[i] = B[i]
        else:
            return []

        A_sum[i] = A_sum[i-1] + A[i]
    return A
        

if __name__ == "__main__":
    N = int(input())
    B = list(map(int, input().split()))
    A = solution(B)

    if A:
        print(*A)
    else:
        print(-1)