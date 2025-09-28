'''
Level: S1
Time: 19m20s
'''

import sys
input = sys.stdin.readline

alp_to_num = {c: i for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
num_to_alp = {v: k for k, v in alp_to_num.items()}

if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    S = list(input().strip())

    for i in range(N):
        if S[i] == 'A':
            continue

        if 26-alp_to_num[S[i]] <= K:
            K -= 26-alp_to_num[S[i]]
            S[i] = 'A'
    
    if K > 0:
        S[-1] = num_to_alp[(alp_to_num[S[-1]] + K) % 26]
    print(''.join(S))