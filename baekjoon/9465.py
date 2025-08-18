import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    board = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(2) ]
    
    dp = [[0]*(N+2) for _ in range(2)]
    for j in range(N):
        for i in range(2):
            dp[i][j+2] = max(dp[i][j], dp[1-i][j+1], dp[1-i][j]) + board[i][j]

    print(dp[0])
    print(dp[1])
    print(max(dp[0][-1], dp[1][-1]))