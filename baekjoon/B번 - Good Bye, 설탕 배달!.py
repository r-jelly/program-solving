import sys
input = lambda: sys.stdin.readline().strip()

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def solution():
        dp = [[0]*5 for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(3):
                dp[i][j] = max(dp[i-1][j], arr[i-1][j])
                dp[i][3] += dp[i][j]

            if dp[i][3] >= (arr[i-1][3] - (i - 1)):
                return False
        return True
    
    if solution():
        print("YES")
    else:
        print("NO")