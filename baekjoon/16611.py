'''
Level: S4
Time: 46m24s
'''

import sys
N, M = list(map(int, sys.stdin.readline().split()))
A = list(sys.stdin.readline().strip())
B = list(sys.stdin.readline().strip())

alp_to_num = {alp: num for num, alp in enumerate('abcdefghijklmnopqrstuvwxyz')}
num_to_alp = {num: alp for num, alp in enumerate('abcdefghijklmnopqrstuvwxyz')}

K = ["" for _ in range(M)]

for i in reversed(range(M)):
    if i >= M-N:
        a_i = alp_to_num[A[i-(M-N)]]
        b_i = alp_to_num[B[i]]

        K[i] = num_to_alp[(b_i-a_i) % 26]

    else:
        b_i = alp_to_num[B[i]]
        k_j = alp_to_num[K[i+N]]

        K[i] = num_to_alp[(b_i-k_j) % 26]

print(''.join(K + A)[N:])