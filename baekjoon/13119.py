'''
Level: S5
Time: 10m50s
'''

N, M, X = list(map(int, input().split()))
H = list(map(int, input().split()))

board = [["." for _ in range(M)] for _ in range(N)]
for i in range(M):
    for j in range(N-H[i], N):
        board[j][i] = '#'

for i in range(M):
    if board[N-X][i] == "#":
        board[N-X][i] = '*'
    else:
        board[N-X][i] = '-'

    if (i+1)%3 == 0:
        for j in range(N-X+1, N):
            if board[j][i] == '#':
                break
            board[j][i] = '|'

for b in board:
    print(''.join(b))