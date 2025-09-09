'''
Level: S3
Time: 18m43s
'''

K, S, N = list(input().split())

move = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
        'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

K = [col.index(K[0])+1, int(K[1])]
S = [col.index(S[0])+1, int(S[1])]

for _ in range(int(N)):
    op = input()
    dx, dy = move[op]

    next_xk, next_yk = K[0]+dx, K[1]+dy

    if next_xk<1 or next_xk>8 or next_yk<1 or next_yk>8:
        continue
    else:
        if next_xk == S[0] and next_yk == S[1]:
            next_xs, next_ys = S[0]+dx, S[1]+dy

            if next_xs<1 or next_xs>8 or next_ys<1 or next_ys>8:
                continue
            else:
                S = [next_xs, next_ys]
        K = [next_xk, next_yk]

print(f"{col[K[0]-1]}{K[1]}")
print(f"{col[S[0]-1]}{S[1]}")