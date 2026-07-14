N = int(input())

for i in range(2*N):
    # 왼쪽 로고
    print(' ' * (2*N - i - 1), end='')
    print('*', end='')

    if i < N:
        print(' ' * N, end="")
    else:
        print(' ' * (N + 2*(i-N) + 1), end="")
    print('*', end='')

    if i < N:
        print(' ' * (2*i+1), end='')
    else:
        print(' ' * (2*(2*N-i-1)+1), end='')
    print('*', end='')
    
    if i < N:
        print(' ' * (N-i-1), end="")
    else:
        print(' ' * (i-N), end="")
    
    print()